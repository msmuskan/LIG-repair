import subprocess
from timeit import default_timer as timer
import pandas as pd
from pandas.core.common import flatten
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
# from pm4py.objects.log.adapters.pandas import csv_import_adapter as csv_importer #pm4py-1.5.0.1
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from pm4py.visualization.petri_net import visualizer as petrinet_visualizer
from pm4py.visualization.petri_net.variants import token_decoration_frequency
from pm4py.objects.log.obj import EventLog
from pm4py.objects.log.obj import Trace
from pm4py.objects.log.obj import Event
from pm4py.objects.petri_net.obj import PetriNet
from pm4py.objects.petri_net.utils import petri_utils as utils
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from database import query
from pm4py.algo.conformance.alignments.petri_net import algorithm as alignment
from pm4py.algo.evaluation.replay_fitness import algorithm as replay_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization
from progress.bar import IncrementalBar
import random
import argparse
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter
from pm4py.objects.log.exporter.xes import exporter as xes_exporter

""" Function to split the file containing subs. It returns a list
INPUT: -pathubfile: path to the file (e.g. *_new_patterns_filtered.subs)
RETURN: -a: list of sub files
"""


def split_subgraph(pathsubfile):
    var_lettura = open(pathsubfile, "r").readlines()

    a = []
    for x in var_lettura:

        if x != "\n":
            c = x.strip("\n")
            b = c.split(" ")
            for y in b:
                if y == '':
                    b.remove('')
            a.append(b)
    return a


"""
INPUT: -sub_ocmatrix_file: path to the occurrence matrix for the subs (e.g., *_table2_on_file.csv)
       -subname: subgraph
RETURN: list of graphs in which the input subgraph occurs
"""


def list_graph_occurence(sub_ocmatrix_file, subname):
    # df = csv_importer.import_dataframe_from_path(sub_ocmatrix_file, sep=";")  #pm4py-1.5.0.1
    df = pd.read_csv(sub_ocmatrix_file, sep=';')
    graphs = []
    for x in range(len(df)):
        if (df.loc[x]["Sub" + subname] == 1):
            grafo = df.loc[x]['grafo']
            n = grafo[5:]
            graphs.append("graph" + n)
    return graphs


""" 
INPUT: -lista: list of strings representing integers
RETURN: -max: max number in the list
"""


def massimo_lista(lista):
    max = int(lista[0])
    pos = 1
    while pos < len(lista):
        if int(lista[pos]) > max:
            max = int(lista[pos])
        pos = pos + 1
    return max


""" 
INPUT: -lista: list of strings representing integers
RETURN: -min: min number in the list
"""


def minimo_lista(lista):
    min = int(lista[0])
    pos = 1
    while pos < len(lista):
        if int(lista[pos]) < min:
            min = int(lista[pos])
        pos = pos + 1
    return str(min)


"""
INPUT: -places: set of places in a net
RETURN: -new_place: the available name for a new place
"""


def places_name_available(places, transitions):
    place_name = []
    place_number = []
    trans_name = []

    for place in places:
        place_name.append(place.name)
    for trans in transitions:
        trans_name.append(trans.name)
    for x in place_name:
        place_number.append(int(x.split("n")[1]))
    for y in trans_name:
        if y[:1] == "n":
            place_number.append(int(y.split("n")[1]))

    max = massimo_lista(place_number)
    new_place = str(max + 1)
    return new_place


"""
INPUT: -transations: set of transition of the net
RETURN: -new_transation: an available name for a new transition
"""


def transition_hidden_available(transitions):
    trans_name = []
    trans_number = []

    for trans in transitions:
        trans_name.append(trans.name)

    for x in trans_name:
        if x[:1] == "h":
            trans_number.append(int(x.split("h")[1]))

    if (trans_number != []):
        max = massimo_lista(trans_number)
        new_trans = str(max + 1)
        return new_trans
    else:
        return str(1)


"""
INPUT: -transations: set of transitions in the net
RETURN: -new_transation: an available name for a new transition
"""


def transition_name_available(transitions):
    trans_name = []
    trans_number = []

    for trans in transitions:
        trans_name.append(trans.name)

    for x in trans_name:
        if x[:1] == "s":
            trans_number.append(int(x.split("s")[1]))

    if (trans_number != []):
        max = massimo_lista(trans_number)
        new_trans = str(max + 1)
        return new_trans
    else:
        return str(1)


"""
INPUT: -path_file: list of patterns with corresponding subs (e.g., bpmdemo2_new_patterns_filtered.subs)
RETURN: list of patterns (as a list of lists of subs)
"""


# "*_new_patterns_filtered.subs"
def create_patterns_list(path_file):
    patterns = []
    sub = []
    a = split_subgraph(path_file)
    for y in a:
        if y != ['S'] and y[0] != 'd':
            sub.append(y[2][4:])
        elif y == ['S']:
            if sub != []:
                patterns.append(sub)
                sub = []
    patterns.append(sub)
    return patterns


"""
INPUT: -pattern_file: list of patterns with corresponding subs (e.g., bpmdemo2_new_patterns_filtered.subs)
       -pattern_number: index of the pattern in the list
RETURN: list of sub for the input pattern
"""


# "*_new_patterns_filtered.subs"
def list_sub_pattern(pattern_file, pattern_number):
    pattern_list = create_patterns_list(pattern_file)
    list_sub = pattern_list[pattern_number - 1]
    return list_sub


"""
INPUT: -n: index of a sub
       -sub_file: path to a file containing the list of all subgraphs (e.g., nomedataset.subs) 
RETURN: the instance graph of the input sub
"""


# "*.subs"
def sub_graph(n, sub_file):
    var_lettura1 = open(sub_file, "r").readlines()

    i = 0
    c = 0
    for x in var_lettura1:
        if x == 'S\n':
            i = i + 1
            if i == n:
                y1 = c + 1
            elif i == n + 1:
                y2 = c - 1
                break
        c = c + 1

    subgraph = var_lettura1[y1:y2]
    return subgraph


"""
The function writes the file sub_sgiso_input.txt that can be used as a first argument for the sgiso tool
INPUT: -subgrap: sub risultato di sub_graph()
       -pattern: the path "../patterns_file/" 
"""


def write_subfile(subgrap, pattern):
    file = open(pattern + "/graphsub.g", "w")

    for x in subgrap:
        file.write(x)
    file.close()


"""  The function prints the input string to a file
INPUT: -output: string to write in the file
       -pattern: the folder "../patterns_file/"
       -sub: a string representing the id of the sub 
       -mod: opening mode for the file
"""
def write_outputfile(output, pattern, sub, mod):
    print(output)
    file = open(pattern + "output_" + sub + ".txt", mod)
    file.write(output)
    file.write("\n")
    file.close()


"""
The function writes files graphn.g that can be used as input for the tool gm
INPUT: -subgrap: the instance graph of the input sub (i.e. the output of sub_graph())
       -n: graph number
       -pattern: the folder "../patterns_file/"
"""
def write_graphfile(subgrap, n, pattern):
    subcopy = []
    for x in subgrap:
        subcopy.append(x)
    i = 1
    dict = {}

    for x in range(len(subcopy)):
        if subcopy[x] == 'Found':
            break
        elif subcopy[x] == 'v':
            dict[subcopy[x + 1]] = i
            subcopy[x + 1] = i
            i = i + 1
        elif subcopy[x] == 'd' or subcopy[x] == 'e':
            subcopy[x + 1] = dict[subcopy[x + 1]]
            subcopy[x + 2] = dict[subcopy[x + 2]]

    file = open(pattern + "/graph" + n + ".g", "w")

    for x in range(len(subcopy)):
        if subcopy[x] == 'Found':
            break
        elif subcopy[x] == 'v' or subcopy[x] == 'd' or subcopy[x] == 'e':
            file.write('\n' + subcopy[x])
        else:
            file.write(' ' + str(subcopy[x]))
    file.close()


"""
INPUT: -sub_number: the number of a sub (it will be used to get the IG from the sub through sub_graph)
       -graph_number: the number of the graph (IG of the trace) used as input to sgiso
       -pattern: folder "../patterns_file/"
RETURN: the output of the sgiso tool
"""


def find_instances(sub_number, graph_number, pattern):
    subgraph = sub_graph(int(sub_number), pattern + "subelements.txt")

    write_subfile(subgraph, pattern)

    out = subprocess.Popen([pattern + '/sgiso',
                            pattern + '/graphsub.g',
                            pattern + '/graphs/' + graph_number + '.g'],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    sub = stdout.decode("utf-8")
    sub2 = sub.split()

    return sub2


def create_subelements_file(name_database, pattern):
    testo = []
    n = query.query_count_row(name_database)

    for x in range(n):

        riga1 = query.query_with_fetchone(x, name_database)

        if type(riga1) == tuple:
            if riga1[0] == None:
                riga1 = None
        if riga1 == None:
            riga2 = query.query_subcontent(x, name_database)
            if riga2 == None:
                continue
            riga = riga2[0].split(" ")

            if riga[1] != '1':
                a = []
                for x in riga:
                    try:
                        val = int(x)
                    except ValueError:
                        continue
                    if x not in a:
                        a.append(x)
                i = 1
                for y in a:
                    for w in range(len(riga)):
                        try:
                            val = int(riga[w])
                        except ValueError:
                            continue
                        if riga[w] == y:
                            riga[w] = i
                    i = i + 1

            # print(riga)

            testo.append(riga)
        else:
            # print(riga1[0])
            testo.append(riga1[0])

    file = open(pattern + "subelements.txt", "w")

    for y in testo:
        file.write("\nS\n")
        if type(y) == list:
            for k in y:
                file.write(str(k))
                file.write(" ")

        else:
            file.write(str(y))

    file.close()


"""
INPUT: -graph: a sub (i.e. the output of find_instances())
RETURN: start_sub: list of start nodes in the sub, end_sub: list of end nodes in the sub.
"""


def startend_node(graph):
    sub_label = []
    start_edge = []
    end_edge = []
    node = []
    for x in range(len(graph)):
        if graph[x] == "instances.":
            break
        elif graph[x] == "v":
            node.append(graph[x + 1])
            sub_label.append(graph[x + 2])
        elif graph[x] == "d" or graph[x] == "e":
            start_edge.append(graph[x + 1])
            end_edge.append(graph[x + 2])

    start_sub = []
    end_sub = []
    for y in node:
        if start_edge == [] and end_edge == []:
            start_sub.append(y)
            end_sub.append(y)
        # change Laura 17 January; we may have "floating nodes"
        else:
            if y not in start_edge:
                end_sub.append(y)
            if y not in end_edge:
                start_sub.append(y)

    return start_sub, end_sub, sub_label


"""
INPUT: -graph: a sub (i.e. the output of find_instances())
RETURN: start_sub: list of starting nodes of the sub, end_sub: list of ending nodes in the sub
"""


def startend_graph(graph):
    start_edge = []
    end_edge = []
    node = []
    for x in graph:
        if x[0] == "v":
            node.append(x[1])
        elif x[0] == "d" or x[0] == "e":
            start_edge.append(x[1])
            end_edge.append(x[2])

    start_sub = []
    end_sub = []
    for y in node:
        if y not in start_edge:
            end_sub.append(y)
        elif y not in end_edge:
            start_sub.append(y)

    return start_sub, end_sub


"""
INPUT: -graph_number: the number of a graph
       -pattern: the folder "../patterns_file/"
RETURN: id for the alignment
"""


def get_id_mapping(graph_number, pattern):
    file = open(pattern + "traceIdMapping.txt", "r")

    for y in file:
        y1 = []
        i = 0
        for y3 in y:
            if y3 == ";":
                i = i + 1
                break
            else:
                y1.append(y3)
            i = i + 1
        c = "".join(y1)
        if int(c) == graph_number:
            y4 = y[i:]
            break

    file.close()
    return y4


""" The function creates the dict with numTrace and traceId by querying the db
RETURN: -dict_traceid: a dict with pairs 'numTrace':'idTrace'
"""


def create_dict_trace(name_database):
    dict_traceid = {}

    traceid = query.query_with_fetchall(name_database)
    for x in traceid:
        dict_traceid['graph' + x[0]] = x[1]
    return dict_traceid


""" The function returns from the log the trace object corresponding to the input graph
INPUT: -log: an event log
       -dict_trace: a dictionary of pairs idTrace and numTrace
       -graph: the number of the trace
RETURN: -trace: an object of type Trace containing the target trace
"""


def search_trace(log, dict_trace, graph):
    trace = Trace()
    for t in log:
        if t.attributes['concept:name'] == dict_trace[graph]:
            trace = t
    return trace


""" The functions returns the type of move in an aligment
INPUT: -move: a tuple of the alignment with labels on trasitions
RETURN: -"M": move on model
        -"L": move on log
        -"L/M": synchronous move
"""


def def_move(move):
    if move[0] == ">>" and move[1] != ">>":
        return "M"
    elif move[0] != ">>" and move[1] == ">>":
        return "L"
    else:
        return "L/M"


""" The functions takes a graph in input and returns the corresponding alignment
INPUT: -pattern: the folder with the files
       -dict_trace: a dictionarity with pairs idTrace:numTrace
       -graph: the number of a trace
RETURN: -text: the alignment
"""


def search_alignment(pattern, dict_trace, graph):
    lines = open(pattern + "/alignment.csv", "r").readlines()

    if lines[0][:5] != "Index":
        open(pattern + "/alignment.csv", "w").writelines(lines[2:])

    # df = csv_importer.import_dataframe_from_path(pattern + "alignment.csv", sep=",") #pm4py-1.5.0.1
    df = pd.read_csv(pattern + "/alignment.csv", sep=",")

    for j in range(len(df)):

        if df.iloc[j]['Match'] == "NaN":
            break
        else:
            trace_string = df.iloc[j]['Case IDs']
            #if(type(trace_string)=='str'):
            list_trace = trace_string.split('|')

        if dict_trace[graph] in list_trace:
            alignment = df.iloc[j]['Match']
            break
            
    text = alignment.split("|")

    return text


""" The function checks that the input sub occurs in the graphs in the list
INPUT: -graph_list: a list of graph names
       -subnumber: the number of a sub
       -pattern: the folder "../patterns_file/"
RETURN: -graph_list: the list containing only graphs with the input sub
"""


def check_graphlist(graph_list, subnumber, pattern):
    list = []
    for x in graph_list:
        list.append(x)
    bar = IncrementalBar('Correctness check graph_list', max=len(graph_list))
    for x in list:
        sub = find_instances(subnumber, x, pattern)
        if sub[1] == '0':
            graph_list.remove(x)
        else:
            bar.next()
    bar.finish()
    return graph_list


""" The function gets the Raw Fitness Cost, from file alignment.csv, of the trace corresponding to the input graph
INPUT: -pattern: folder including the files
       -dict_trace: a dictionary with pairs idTrace:numTrace
       -graph: the graph name
RETURN: -float(cost): Raw Fitness Cost
"""


def search_fitness_cost(pattern, dict_trace, graph):
    lines = open(pattern + "alignment.csv", "r").readlines()

    if lines[0][:5] != "Index":
        open(pattern + "alignment.csv", "w").writelines(lines)

    # df = csv_importer.import_dataframe_from_path(pattern + "alignment.csv", sep=",") #pm4py1.5.0.1
    df = pd.read_csv(pattern + "alignment.csv", sep=",")

    for j in range(len(df)):
        if df.loc[j]['Match'] == "NaN":
            break
        else:
            trace_string = df.loc[j]['Case IDs']
            list_trace = trace_string.split('|')

        if dict_trace[graph] in list_trace:
            cost = df.loc[j]['Raw Fitness Cost']
            break

    return float(cost)


""" The function gets the Raw Fitness Cost, from file alignment.csv, of the trace corresponding to the input graph
INPUT: -pattern: folder including the files
       -dict_trace: a dictionary with pairs idTrace:numTrace
       -graph_list: a list of graphs in which the target sub occurs
RETURN: -first_trace: a graph with the smallest Raw Fitness Cost
        -mincost: Raw Fitness Cost
"""


def select_graph(pattern, dict_trace, graphlist):
    mincost = search_fitness_cost(pattern, dict_trace, graphlist[0])
    mintracelist = []
    for x in graphlist:
        cost = search_fitness_cost(pattern, dict_trace, x)
        if cost < mincost:
            mincost = cost
            mintracelist = []
            mintracelist.append(x)
        elif cost == mincost:
            mintracelist.append(x)

    first_trace = random.choice(mintracelist)
    # print("Raw Fitness Cost: ", mincost, "Graph list: ", mintracelist)
    return first_trace, mincost


""" The function searches in the input alignment the position of the start transition of the graph, counting synchronous/log moves. 
    For each start node, it takes all transitions before the identified point, only considering moves on model and synchronous moves. Then it applies a
    token-based replay, obtaining the reached_marking.
INPUT: -pattern: the folder containing the files
       -dataset: the dataset name
       -trace: the trace name
       -start: a list of start nodes in the graph
RETURN: -reached_marking: a dictionary with pairs 'start':'marking'
"""


def dirk_marking_start(dataset, start, text, trace, pattern, sub):
    net, initial_marking, final_marking = pnml_importer.apply(pattern + "/" + dataset +'_petriNet.pnml')
    new_trace = Trace(attributes=trace.attributes)
    im = str(initial_marking).strip('[]\'').split(':')
    i_marking = im[0]
    m = minimo_lista(start)

    k = 0
    reached_marking = []
    del_event = []
    g = 0
    for w in text:
        if int(m) == 1:
            break
        elif k == int(m):
            break

        if w[:3] == "[L]":
            k = k + 1
            g = g + 1
            if k != int(m):
                for d in del_event:
                    new_trace.append(d)
                del_event = []
        elif w[:5] == "[L/M]":
            k = k + 1
            if k != int(m):

                for d in del_event:
                    new_trace.append(d)
                del_event = []
                new_trace.append(trace[g])
                g = g + 1

        elif w[:8] == "[M-REAL]" or w[:8] == "[M-INVI]":
            event = Event()
            event['org:resource'] = 'NONE'
            event['lifecycle:transition'] = 'complete'
            event['concept:name'] = w[8:]
            del_event.append(event)

    if k > 1:

        new_log = EventLog()
        new_log.append(new_trace)

        replayed_traces = token_replay.apply(new_log, net, initial_marking, final_marking, parameters={"try_to_reach_final_marking_through_hidden":False})
        # print("Token-based Replay: ", replayed_traces)
        write_outputfile("Token-based Replay:  " + str(replayed_traces), pattern, sub, "a")
        #count=0
        #for u in replayed_traces[0]['activated_transitions']:
        #    count = count + 1

        #if(count>g):
        #    print(trace[g-1]['concept:name'])
        #    for tr in net.transitions:
        #        if(tr.label==trace[g-1]['concept:name']):
        #            for pl in net.places:
        #                for arc in pl.out_arcs:
        #                    if arc.target.name == tr.name:
        #                        reached_marking.append(pl.name)

        #    print('Correct Reached Marking ---- >',reached_marking)
        #else:
        for v in replayed_traces[0]['reached_marking']:
            reached_marking.append(v.name)
    else:
        reached = i_marking
        reached_marking.append(reached.split(":")[0])

    return reached_marking


""" The function searches in the input alignment the position of the end transition of the graph, counting synchronous/log moves. 
    For each end node, it takes all transitions before the identified point, only considering moves on model and synchronous moves. Then it applies a
    token-based replay, obtaining the reached_marking.
INPUT: -pattern: the folder containing the files
       -dataset: the dataset name
       -trace: the trace name
       -end: a list of start nodes in the graph
RETURN: -reached_marking: a dictionary with pairs 'end':'marking'

"""


def dirk_marking_end(dataset, end, text, trace, pattern, sub):
    net, initial_marking, final_marking = pnml_importer.apply(pattern + "/" + dataset+ '_petriNet.pnml')
    reached_marking = []
    m = str(massimo_lista(end))

    k = 0
    new_trace = Trace(attributes=trace.attributes)
    g = 0
    for w in text:

        if w[:3] == "[L]":

            k = k + 1
            if k > int(m):
                break
            g = g + 1

        elif w[:5] == "[L/M]":
            k = k + 1

            if k > int(m):
                break

            new_trace.append(trace[g])
            g = g + 1

        elif w[:8] == "[M-REAL]" or w[:8] == "[M-INVI]":
            event = Event()
            event['org:resource'] = 'NONE'
            event['lifecycle:transition'] = 'complete'
            event['concept:name'] = w[8:]
            new_trace.append(event)

    if k > 1:

        new_log = EventLog()
        new_log.append(new_trace)
        replayed_traces = token_replay.apply(new_log, net, initial_marking, final_marking, parameters={"try_to_reach_final_marking_through_hidden":False})
        # print("Token-based Replay: ", replayed_traces)
        write_outputfile("Token-based Replay:  " + str(replayed_traces), pattern, sub, "a")

        #count = 0
        #for u in replayed_traces[0]['activated_transitions']:
        #    count = count + 1

        #if (count > g):
        #    print(trace[g - 1]['concept:name'])
        #    for tr in net.transitions:
        #        if (tr.label == trace[g - 1]['concept:name']):
        #            for pl in net.places:
        #                for arc in pl.out_arcs:
        #                    if arc.target.name == tr.name:
        #                        reached_marking.append(pl.name)

        #    print('Correct Reached Marking ---- >', reached_marking)
        #else:
        for v in replayed_traces[0]['reached_marking']:
            reached_marking.append(v.name)

    return reached_marking


""" The functions simplifies a sub, by removing the part that cannot be followed. 
By checking the alignment the sub is cut until a move on model/log is found
INPUT: -start: a list with the start nodes of the sub
       -text: the alignment
       -subgraph: the output of find_instances()
RETURN: a subgraph
"""


def start_pre_process_repairing(start, text, subgraph):
    m = minimo_lista(start)
    k = 1
    del_event = []

    for w in text:

        if k >= int(m):
            if w[:3] == "[L]":
                break
            elif w[:5] == "[L/M]":
                del_event.append(w[5:])
            elif w[:8] == "[M-REAL]" or w[:8] == "[M-INVI]":
                break

        elif w[:3] == "[L]":
            k = k + 1
        elif w[:5] == "[L/M]":
            k = k + 1
        elif w[:8] == "[M-REAL]" or w[:8] == "[M-INVI]":
            continue

    number = []
    for y in del_event:
        j = 0
        for p in subgraph:
            if y == p:
                p1 = j - 2
                p2 = j + 1
                number.append(subgraph[j - 1])
                del subgraph[p1:p2]
                break
            j = j + 1

    for n in number:
        j = 0
        for q in range(len(subgraph)):
            if subgraph[j] == 'Found':
                break
            elif subgraph[j] == 'd' and (subgraph[j + 1] == n or subgraph[j + 2] == n):
                del subgraph[j:j + 4]
            else:
                j = j + 1

    return subgraph


"""
 The functions simplifies a sub, by removing the part that cannot be followed. 
By checking the alignment the sub is cut from the end until a move on model/log is found
INPUT: -end: a list with the end nodes of the sub
       -text: the alignment
       -subgraph: the output of find_instances()
RETURN: a subgraph

NOTE: 07/21 bug fix: if the final node is [L/M] and before there is a [M], the end node was not correctly deleted.
"""


def end_pre_process_repairing(end, text, subgraph):
    m = massimo_lista(end)
    k = 1
    x = 0
    q = 0 #mi serve per controllare che quando k==m siamo sul nodo finale corretto.
    del_event = []

    for w in text:
        if k == m:
            while k == m:
                if text[x][:3] == "[L]":
                    q = q +1
                    break
                elif text[x][:5] == "[L/M]":
                    del_event.append(text[x][5:])
                    x = x - 1
                    q = q +1
                elif text[x][:8] == "[M-REAL]" or text[x][:8] == "[M-INVI]":
                    if q == 0:
                        x = x + 1
                        continue
                    break
            break
        elif w[:3] == "[L]":
            k = k + 1
        elif w[:5] == "[L/M]":
            k = k + 1
        elif w[:8] == "[M-REAL]" or w[:8] == "[M-INVI]":
            x = x + 1
            continue

        x = x + 1

    number = []
    subgraph.reverse()
    for y in del_event:
        j = 0
        for p in subgraph:
            if y == p:
                p1 = j
                p2 = j + 3
                number.append(subgraph[j + 1])
                del subgraph[p1:p2]
                break
            j = j + 1

    subgraph.reverse()
    for n in number:
        j = 0
        for q in range(len(subgraph)):
            if subgraph[j] == 'Found':
                break
            elif subgraph[j] == 'd' and (subgraph[j + 1] == n or subgraph[j + 2] == n):
                del subgraph[j:j + 4]
            else:
                j = j + 1

    return subgraph


""" The function create the Petri net of the input subgraph and returns the start/end Transition objects in two dictionaries
INPUT: -subgraph: the output of find_instances()
       -net: the net model
       -start: list of the sub's start nodes
       -end: list of the sub's start nodes
RETURN: -start_result, end_result: dictionaries 'number_node_start':'corresponding_object_Transitions'
"""


def create_sub_petrinet(subgraph, net, start, end, pattern, sub):
    transitions = net.transitions
    places = net.places
    place_number = []
    arc = []
    place_dict = {}
    trans_dict = {}

    for x in range(len(subgraph)):
        if subgraph[x] == "Found":
            break
        elif subgraph[x] == 'd' or subgraph[x] == 'e':
            arc.append((subgraph[x + 1], subgraph[x + 2]))
            if subgraph[x + 2] not in place_number:
                n = places_name_available(places, transitions)
                place = PetriNet.Place("n" + n)
                net.places.add(place)
                place_dict[subgraph[x + 2]] = place
                place_number.append(subgraph[x + 2])
            else:
                n = places_name_available(places, transitions)
                place = PetriNet.Place("n" + n)
                net.places.add(place)
                place_dict[str(subgraph[x + 1]) + str(subgraph[x + 2])] = place
        elif subgraph[x] == 'v':
            n = transition_name_available(transitions)
            trans = PetriNet.Transition("s" + n, subgraph[x + 2])
            net.transitions.add(trans)
            trans_dict[subgraph[x + 1]] = trans

    for y in arc:
        ap = str(y[0]) + str(y[1])
        if y[1] in place_number:
            utils.add_arc_from_to(trans_dict[y[0]], place_dict[y[1]], net)
            write_outputfile(
                "Added:  " + str(trans_dict[y[0]].label) + " " + str(trans_dict[y[0]].name) + " --> " + str(
                    place_dict[y[1]]), pattern, sub, "a")
            # print("Added: ", trans_dict[y[0]].label, trans_dict[y[0]].name, "-->", place_dict[y[1]])
            utils.add_arc_from_to(place_dict[y[1]], trans_dict[y[1]], net)
            write_outputfile("Added:  " + str(place_dict[y[1]]) + " --> " + str(trans_dict[y[1]].label) + " " + str(
                trans_dict[y[1]].name), pattern, sub, "a")
            # print("Added: ",place_dict[y[1]], "-->", trans_dict[y[1]].label, trans_dict[y[1]].name)
            place_number.remove(y[1])
        elif ap in place_dict:
            utils.add_arc_from_to(trans_dict[y[0]], place_dict[ap], net)
            write_outputfile(
                "Added:  " + str(trans_dict[y[0]].label) + " " + str(trans_dict[y[0]].name) + " --> " + str(
                    place_dict[ap]), pattern, sub, "a")
            # print("Added: ", trans_dict[y[0]].label, trans_dict[y[0]].name, "-->", place_dict[ap])
            utils.add_arc_from_to(place_dict[ap], trans_dict[y[1]], net)
            write_outputfile("Added:  " + str(place_dict[ap]) + " --> " + str(trans_dict[y[1]].label) + " " + str(
                trans_dict[y[1]].name), pattern, sub, "a")
            # print("Added: ",place_dict[ap], "-->", trans_dict[y[1]].label, trans_dict[y[1]].name)

    start_result = {}
    end_result = {}
    start_result['start'] = trans_dict[minimo_lista(start)].name
    end_result['end'] = trans_dict[str(massimo_lista(end))].name
    for s in start:
        start_result[s] = trans_dict[s]
    for e in end:
        end_result[e] = trans_dict[e]

    return start_result, end_result


""" The function repairs the subgraph with the net
INPUT: -subgraph: the output of find_instances()
       -net: the net model
       -start: list of the sub's start nodes
       -end: list of the sub's start nodes
       -start_marking: the output of dirk_marking_start()
       -end_marking: the output of  dirk_marking_end()
"""


def repairing(subgraph, net, initial_marking, final_marking, start, end, start_marking, end_marking, pattern, sub):
    start_trans, end_trans = create_sub_petrinet(subgraph, net, start, end, pattern, sub)

    places = net.places
    transitions = net.transitions

    if len(start) > 1:
        n = transition_hidden_available(transitions)
        t = PetriNet.Transition("h" + n, None)
        net.transitions.add(t)
        for v in start_marking:
            for place in net.places:
                if place.name == v:
                    utils.add_arc_from_to(place, t, net)
                    write_outputfile("Added: " + str(place) + " -- > " + str(t) + " " + str(t.name), pattern, sub, "a")
                    # print("Added: ", place, " -- > ", t, t.name)
        for x in start:
            n = places_name_available(places, transitions)
            place = PetriNet.Place("n" + n)
            net.places.add(place)
            utils.add_arc_from_to(t, place, net)
            write_outputfile("Added:  " + str(t) + " " + str(t.name) + " -- > " + str(place), pattern, sub, "a")
            # print("Added: ", t, t.name, " -- > ", place)
            utils.add_arc_from_to(place, start_trans[x], net)
            write_outputfile("Added: " + str(place) + " -- > " + str(start_trans[x]) + " " + str(start_trans[x].name),
                             pattern, sub, "a")
            # print("Added: ", place, " -- > ", start_trans[x], start_trans[x].name)
    else:
        for v in start_marking:
            for place in net.places:
                if place.name == v:
                    utils.add_arc_from_to(place, start_trans[start[0]], net)
                    write_outputfile("Added: " + str(place) + " -- > " + str(start_trans[start[0]]) + " " + str(
                        start_trans[start[0]].name), pattern, sub, "a")
                    # print("Added: ", place, " -- > ", start_trans[start[0]], start_trans[start[0]].name)

    if len(end) > 1:
        n = transition_hidden_available(transitions)
        t = PetriNet.Transition("h" + n, None)
        net.transitions.add(t)
        for y in end_marking:
            for place in net.places:
                if place.name == y:
                    utils.add_arc_from_to(t, place, net)
                    write_outputfile("Added: " + str(t) + " " + str(t.name) + " --> " + str(place), pattern, sub, "a")
                    # print("Added: ", t, t.name, " --> ", place)
        for x in end:
            n = places_name_available(places, transitions)
            place = PetriNet.Place("n" + n)
            net.places.add(place)
            utils.add_arc_from_to(place, t, net)
            write_outputfile("Added: " + str(place) + " -- > " + str(t), pattern, sub, "a")
            # print("Added: ", place, " -- > ", t)
            utils.add_arc_from_to(end_trans[x], place, net)
            write_outputfile("Added: " + str(end_trans[x]) + " " + str(end_trans[x].name) + " -- > " + str(place),
                             pattern, sub, "a")
            # print("Added: ", end_trans[x], end_trans[x].name, " -- > ", place)
    else:
        for v in end_marking:
            for place in net.places:
                if place.name == v:
                    utils.add_arc_from_to(end_trans[end[0]], place, net)
                    write_outputfile(
                        "Added: " + str(end_trans[end[0]]) + " " + str(end_trans[end[0]].name) + " -- > " + str(place),
                        pattern, sub, "a")
                    # print("Added: ", end_trans[end[0]], end_trans[end[0]].name, " -- > ", place)

    start_end_trans = [start_trans['start'], end_trans['end']]
    return start_end_trans, net


""" The function repairs the model adding a hidden transition between the last nodes of the subs and the model and the end node
INPUT: -net: the net model
       -arcs: set of arcs in the net
       -places: set of places in the net
       -transitions: set of transitions in the net
"""


def hidden_end_transitions(net, arcs, places, transitions, final_marking, pattern, sub):
    fm = str(final_marking).strip('[]\'').split(':')
    f_marking = fm[0]
    n = transition_hidden_available(transitions)
    h = PetriNet.Transition("h" + n, None)
    net.transitions.add(h)
    write_outputfile("Added:  " + str(h.label) + " " + str(h.name), pattern, sub, "a")
    # print("Added: ", h.label, h.name)

    ar = []
    for trans in transitions:
        for arc in trans.out_arcs:
            if arc.target.name == f_marking:
                ar.append(arc)
                n = places_name_available(places, transitions)
                pl = PetriNet.Place("n" + n)
                net.places.add(pl)
                write_outputfile("Added:  " + str(pl), pattern, sub, "a")
                # print("Added: ", pl)
                utils.add_arc_from_to(trans, pl, net)
                write_outputfile("Added:  " + str(trans.label) + " " + str(trans.name) + " --> " + str(pl), pattern,
                                 sub, "a")
                # print("Added: ", trans.label, trans.name, " --> ", pl)
                utils.add_arc_from_to(pl, h, net)
                write_outputfile("Added:  " + str(pl) + " --> " + str(h.label) + " " + str(h.name), pattern, sub, "a")
                # print("Added: ", pl, " --> ", h.label, h.name)
                break
    for a in ar:
        remove_arc(net, a)
    for p in places:
        if p.name == f_marking:
            utils.add_arc_from_to(h, p, net)
            write_outputfile("Added:  " + str(h.label) + " " + str(h.name) + " --> " + str(p), pattern, sub, "a")
            # print("Added: ", h.label, h.name, " --> ", p)


""" The function finds the position of the alignment in the sub
INPUT: -al: an alignment
       -start: the name of the start transition in the sub
       -end: the name of the end transition in the sub
RETURN: -pos_start: the index of the alignment list corresponding to the start node
        -pos_end: the index of the alignment list corresponding to the start node
"""


def pos_node_alignment(al, start, end):
    i = 0
    pos_start = 0
    pos_end = 0

    for a in al[0]['alignment']:
        if a[0][1] == end and a[0][1] == start:
            pos_end = i
            pos_start = i
            break
        elif a[0][1] == end:
            pos_end = i
            break
        elif a[0][1] == start:
            pos_start = i
        i = i + 1

    return pos_start, pos_end


""" The function removes an arc from a Petri net
INPUT: -net: Petri net
       -arc: Arc of the Petri net
RETURNS: -net: Petri net
"""


def remove_arc(net, arc):
    net.arcs.remove(arc)
    arc.source.out_arcs.remove(arc)
    arc.target.in_arcs.remove(arc)

    return net


""" The function checks that the repairment is necessary, in case the outgoing arcs of the two hidden transition (h1,h2) 
are directed to the same places
INPUT: -trans: a transition 
       -tr: a transition
       -places: list of places of the net
RETURN: -True: if repairment with the hidden transition is necessary
        -False: if repairment is not necessary
"""


def check_rep_ltrans(c_trans, c_tr, c_places):
    h1_add=[]
    h2_add=[]
    result = True
    for c_place in c_places:
        for arc in c_place.out_arcs:
            if arc.target.name == c_trans.name:
                h1_add.append(c_place.name)
        for at in c_place.in_arcs:
            if at.source.name == c_tr.name:
                h2_add.append(c_place.name)
    if (len(h1_add) == len(h2_add)):
        i = 0
        for p in h1_add:
            if p in h2_add:
                i = i + 1
        if i == len(h1_add):
            result = False

    return result



""" The function repairs the model a second time in order to make the input trace fit, 
fixing the move on log step by step
INPUT: -trace: the target trace
       -start: name of the start transition
       -end: name of the end transition
       -net: the net model
       -initial_marking: initial marking of the model
       -final_marking: ending marking of the model
       -sub: list of transition labels for the sub
       -pattern: path for 'patterns_file'
       -nsub: number of the sub 
RETURN: -'U': if the sub is perfectly fitting with no need to add arcs
        -'UA': some arcs have been added to make the sub fitting
        -'UNA': the sub was not followed in the alignment
        -'UNG': the case was not managed
"""


def first_postrepairing_algorithm(trace, start, end, net, initial_marking, final_marking, sub, pattern, nsub):
    new_log = EventLog()
    new_log.append(trace)

    al = alignment.apply_log(new_log, net, initial_marking, final_marking, parameters={"ret_tuple_as_trans_desc": True})

    write_outputfile("New Alignment  " + trace.attributes['concept:name'] + ":  " + str(al), pattern, nsub, "a")

    move = al[0]['alignment']
    places = net.places
    transitions = net.transitions
    arcs = net.arcs

    pos_start, pos_end = pos_node_alignment(al, start, end)
    added = 0
    pos = pos_start
    deleted_arc = []
    t_to_add = []
    p_to_add = []
    a_to_add = []
    name_p = []
    n = int(transition_hidden_available(transitions))
    caso = False
    p = ""

    # Here we check that the case M-L is not in the alignment (still not managed)
    # To do:
    # if a [M/L] is present -> add a HIDDEN TRANSITION between the previous and the next activity
    while pos <= pos_end:
        if def_move(move[pos][1]) == 'L' and def_move(move[pos - 1][1]) == 'M' and move[pos - 1][1][1] != None:
            caso = True
            break
        elif def_move(move[pos][1]) == 'L' and def_move(move[pos + 1][1]) == 'M' and move[pos + 1][1][1] != None:
            caso = True
            break
        pos = pos + 1

    pos = pos_start
    if pos_start != 0 and caso != True:
        pos_second_transition = ""
        while pos <= pos_end:
            if def_move(move[pos][1]) == 'L':
                justrep2 = []
                pos_transition = ""
                if p == "":
                    p = places_name_available(places, transitions)
                    pl1 = PetriNet.Place("n" + p)
                elif def_move(move[pos - 1][1]) == 'L/M':
                    p = int(p) + 1
                    pl1 = PetriNet.Place("n" + str(p))
                for trans in transitions:
                    if (def_move(move[pos - 1][1]) == 'L/M' or move[pos - 1][1][1] == None) and trans.name == \
                            move[pos - 1][0][1]:
                        justrep = []
                        for tr in transitions:
                            if tr.label in sub:
                                if tr.label == move[pos][1][0] and tr.name[:1] == "s":
                                    if tr.label not in justrep:  # serve per non far ripetere la riparazione due volte nel caso in cui ci fossero nella sub due transition con stessa label e name diversi (a seguito del controllo solo sulla s del name)
                                        pos_transition = tr.name  # trovata la prima volta la transition in pos, le altre volte salto questi controlli e la trovo per name
                                        justrep.append(tr.label)
                                        if check_rep_ltrans(trans, tr, places):
                                            p_to_add.append(pl1)
                                            a_to_add.append((trans, pl1))
                                            h1 = PetriNet.Transition("h" + str(n), None)
                                            n = n + 1
                                            t_to_add.append(h1)
                                            a_to_add.append((pl1, h1))
                                            h2 = PetriNet.Transition("h" + str(n), None)
                                            n = n + 1
                                            t_to_add.append(h2)
                                            a_to_add.append((pl1, h2))
                                            for place1 in places:
                                                for arc in place1.out_arcs:
                                                    if arc.target.name == tr.name:
                                                        a_to_add.append((h1, place1))
                                                        added = added + 1
                                                for at in place1.in_arcs:
                                                    if at.source.name == trans.name:
                                                        a_to_add.append((h2, place1))
                                                        deleted_arc.append(at)
                                                        name_p.append(place1.name)
                                        else:
                                            write_outputfile(
                                                "CASE 4) Repairment is not necessary [" + str(
                                                    trans.name) + ' ' + str(
                                                    trans.label) + ", " + str(tr.name) + ' ' + str(tr.label) + ']',
                                                pattern, nsub, "a")
                            else:
                                if tr.label == move[pos][0][1] and tr.name[:1] == "h":
                                    write_outputfile(
                                        "!!! ERROR(1): tr è un hidden transition --> " + str(tr.name) + " - " + str(
                                            trans.name), pattern, nsub, "a")
                                if tr.label == move[pos][1][0] and tr.name[:1] == "n":
                                    if tr.label not in justrep:
                                        pos_transition = tr.name
                                        justrep.append(tr.label)
                                        if check_rep_ltrans(trans, tr, places):
                                            p_to_add.append(pl1)
                                            a_to_add.append((trans, pl1))
                                            h1 = PetriNet.Transition("h" + str(n), None)
                                            n = n + 1
                                            t_to_add.append(h1)
                                            a_to_add.append((pl1, h1))
                                            h2 = PetriNet.Transition("h" + str(n), None)
                                            n = n + 1
                                            t_to_add.append(h2)
                                            a_to_add.append((pl1, h2))
                                            for place2 in places:
                                                for arc in place2.out_arcs:
                                                    if arc.target.name == tr.name:
                                                        a_to_add.append((h1, place2))
                                                        added = added + 1
                                                for at in place2.in_arcs:
                                                    if at.source.name == trans.name:
                                                        a_to_add.append((h2, place2))
                                                        deleted_arc.append(at)
                                                        name_p.append(place2.name)
                                        else:
                                            write_outputfile(
                                                "CASE 4) Repairment is not necessary [" + str(
                                                    trans.name) + ' ' + str(
                                                    trans.label) + ", " + str(tr.name) + ' ' + str(tr.label) + ']',
                                                pattern, nsub, "a")
                    '''
                    else:
                        for tr in transitions:
                            if tr.name == pos_transition:
                                p_to_add.append(pl1)
                                a_to_add.append((trans, pl1))
                                h1 = PetriNet.Transition("h" + str(n), None)
                                n = n + 1
                                t_to_add.append(h1)
                                a_to_add.append((pl1, h1))
                                h2 = PetriNet.Transition("h" + str(n), None)
                                n = n + 1
                                t_to_add.append(h2)
                                a_to_add.append((pl1, h2))
                                for place1 in places:
                                    for arc in place1.out_arcs:
                                        if arc.target.name == tr.name:
                                            a_to_add.append((h1, place1))
                                            added = added + 1
                                    for at in place1.in_arcs:
                                        if at.source.name == trans.name:
                                            a_to_add.append((h2, place1))
                                            deleted_arc.append(at)
                                            name_p.append(place1.name)
                    '''
                for trans in transitions:
                    if (def_move(move[pos + 1][1]) == 'L/M' or move[pos + 1][1][1] == None) and trans.name == \
                            move[pos + 1][0][1]:
                        # justrep = []
                        if name_p != []:
                            if pos_transition != "":
                                for tr in transitions:
                                    if tr.name == pos_transition:
                                        # if tr.label in sub:
                                        # if tr.label == move[pos][1][0] and tr.name[:1] == "s":
                                        # if tr.label not in justrep:
                                        # pos_transition = tr.name
                                        # justrep.append(tr.label)
                                        h = PetriNet.Transition("h" + str(n), None)
                                        n = n + 1
                                        for place3 in places:
                                            for arc in place3.in_arcs:
                                                if arc.source.name == tr.name:
                                                    t_to_add.append(h)
                                                    a_to_add.append((place3, h))
                                                    if len(name_p) > 1:
                                                        a_to_add.append((h, pl1))
                                                        name_p = []
                                                    added = added + 1
                                            if len(name_p) == 1 and place3.name == name_p[0]:
                                                a_to_add.append((h, place3))
                                                name_p = []
                                    ''' 
                                    else:
                                        if tr.label == move[pos][0][1] and tr.name[:1] == "h":
                                            write_outputfile("!!! ERROR(1): tr è un hidden transition --> " + str(tr.name) + " - " + str(trans.name), pattern, nsub, "a")
                                        if tr.label == move[pos][1][0] and tr.name[:1] == "n":
                                            if tr.label not in justrep:
                                                pos_transition = tr.name
                                                justrep.append(tr.label)
                                                h = PetriNet.Transition("h" + str(n), None)
                                                n = n + 1
                                                for place4 in places:
                                                    inarcs = place4.in_arcs
                                                    for arc in inarcs:
                                                        if arc.source.name == tr.name:
                                                            t_to_add.append(h)
                                                            a_to_add.append((place4, h))
                                                            if len(name_p) > 1:
                                                               a_to_add.append((h,pl1))
                                                               name_p = []
                                                            added = added + 1
                                                    if len(name_p) == 1 and place4.name == name_p[0]:
                                                        a_to_add.append((h, place4))
                                                        name_p = []
                                    '''
                            else:
                                for tr in transitions:
                                    if tr.name == pos_second_transition:
                                        h = PetriNet.Transition("h" + str(n), None)
                                        n = n + 1
                                        for place3 in places:
                                            for arc in place3.in_arcs:
                                                if arc.source.name == tr.name:
                                                    t_to_add.append(h)
                                                    a_to_add.append((place3, h))
                                                    if len(name_p) > 1:
                                                        a_to_add.append((h, pl1))
                                                        name_p = []
                                                    added = added + 1
                                            if len(name_p) == 1 and place3.name == name_p[0]:
                                                a_to_add.append((h, place3))
                                                name_p = []
                for trans in transitions:
                    if def_move(move[pos + 1][1]) == 'L' and trans.label == move[pos+1][1][0] and trans.name[:1] == "s":
                        if trans.label not in justrep2:
                            justrep2.append(trans.label)
                            if pos_transition == "":
                                pos_transition = pos_second_transition
                            pos_second_transition = trans.name
                            for tr in transitions:
                                if tr.name == pos_transition:
                                    if check_rep_ltrans(trans, tr, places):
                                        p = int(p) + 1
                                        pl2 = PetriNet.Place("n" + str(p))
                                        p_to_add.append(pl2)
                                        a_to_add.append((tr, pl2))
                                        h1 = PetriNet.Transition("h" + str(n), None)
                                        n = n + 1
                                        t_to_add.append(h1)
                                        a_to_add.append((pl2, h1))
                                        h2 = PetriNet.Transition("h" + str(n), None)
                                        n = n + 1
                                        t_to_add.append(h2)
                                        a_to_add.append((pl2, h2))
                                        for place5 in places:
                                            for arc in place5.out_arcs:
                                                if arc.target.name == trans.name:
                                                    a_to_add.append((h1, place5))
                                                    added = added + 1
                                            for at in place5.in_arcs:
                                                if at.source.name == tr.name:
                                                    a_to_add.append((h2, place5))
                                                    deleted_arc.append(at)
                                                    # name_p.append(place5.name)
                                    else:
                                        write_outputfile(
                                            "CASE 4) Repairment is not necessary [" + str(trans.name) + ' ' + str(
                                                trans.label) + ", " + str(tr.name) + ' ' + str(tr.label) + ']',
                                            pattern, nsub, "a")
                    else:
                        if def_move(move[pos + 1][1]) == 'L' and trans.label == move[pos+1][1][0] and trans.name[
                                                                                                    :1] == "n":
                            if trans.label not in justrep2:
                                justrep2.append(trans.label)
                                if pos_transition == "":
                                    pos_transition = pos_second_transition
                                pos_second_transition = trans.name
                                for tr in transitions:
                                    if tr.name == pos_transition:
                                        if check_rep_ltrans(trans, tr, places):
                                            p = int(p) + 1
                                            pl2 = PetriNet.Place("n" + str(p))
                                            p_to_add.append(pl2)
                                            a_to_add.append((tr, pl2))
                                            h1 = PetriNet.Transition("h" + str(n), None)
                                            n = n + 1
                                            t_to_add.append(h1)
                                            a_to_add.append((pl2, h1))
                                            h2 = PetriNet.Transition("h" + str(n), None)
                                            n = n + 1
                                            t_to_add.append(h2)
                                            a_to_add.append((pl2, h2))
                                            for place5 in places:
                                                for arc in place5.out_arcs:
                                                    if arc.target.name == trans.name:
                                                        a_to_add.append((h1, place5))
                                                        added = added + 1
                                                for at in place5.in_arcs:
                                                    if at.source.name == tr.name:
                                                        a_to_add.append((h2, place5))
                                                        deleted_arc.append(at)
                                                        # name_p.append(place5.name)
                                        else:
                                            write_outputfile(
                                                "CASE 4) Repairment is not necessary [" + str(trans.name) + ' ' + str(trans.label) + ", " + str(tr.name) + ' ' + str(tr.label) + ']',
                                                pattern, nsub, "a")
            pos = pos + 1

        if len(deleted_arc) != 0:
            for a in deleted_arc:
                try:
                    remove_arc(net, a)
                    write_outputfile("Deleted:  " + str(a), pattern, nsub, "a")
                except:
                    write_outputfile(
                        "!!! ERROR(2): remove_arc failed, trying to remove a nonexistent arc " + str(
                            tr.name) + " - " + str(trans.name), pattern, nsub, "a")
                    continue
        if len(t_to_add) != 0:
            for t in t_to_add:
                transitions.add(t)
        if len(p_to_add) != 0:
            for p in p_to_add:
                places.add(p)
        if len(a_to_add) != 0:
            for ar in a_to_add:
                utils.add_arc_from_to(ar[0], ar[1], net)
                write_outputfile("Added:  " + str(ar[0]) + " --> " + str(ar[1]), pattern, nsub, "a")
                # print("Added: ", ar[0], " --> ", ar[1])
        if added == 0:
            write_outputfile("The sub is perfectly fitting!", pattern, nsub, "a")
            # print("La sub fitta perfettamente!")
            return 'U'
        else:
            list = [net, initial_marking, final_marking]
            return list
    elif pos_start == 0:
        #write_outputfile("New Alignment  " + trace.attributes['concept:name'] + ":  " + str(al), pattern, nsub, "a")
        write_outputfile("The sub was not followed in the alignment!", pattern, nsub, "a")
        # print("New Alignment " + trace.attributes['concept:name'] + ": ", al)
        # print("La sub non e' stata percorsa nell'alignment!")
        return 'UNA'
    elif caso:
        write_outputfile("The case is not managed", pattern, nsub, "a")
        # ("E' presente il caso non gestito!")
        return 'UNG'


""" The function repairs the model a second time connecting the first transition of the sub to the places enabling
the transition of the first move on log in the alignment. This is done by adding an arc going from the places in which the firing of the transition (of the last move on log in the alignment) put a token  
    to the next transition in the log.
INPUT: -trace: the target trace
       -start: name of the start transition
       -end: name of the end transition
        -net: the net model
      -initial_marking: initial marking of the model
       -final_marking: ending marking of the model
       -sub: list of the labels for the transitions in the sub
RETURN: -'U': if the sub is perfectly fitting with no need to add arcs
        -'UA': some arcs have been added to make the sub fitting
        -'UNA': the sub was not followed in the alignment
"""


def second_postrepairing_algorithm(trace, start, end, net, initial_marking, final_marking, sub):
    new_log = EventLog()
    new_log.append(trace)

    al = alignment.apply_log(new_log, net, initial_marking, final_marking, parameters={"ret_tuple_as_trans_desc": True})
    print("New Alignment " + trace.attributes['concept:name'] + ": ", al)

    places = net.places
    transitions = net.transitions
    move = al[0]['alignment']
    pos_start, pos_end = pos_node_alignment(al, start, end)
    added = 0
    pos1 = pos_start
    first = ''
    last = ''
    pos_last = 0

    if pos_start != 0:
        while pos1 < pos_end:

            if def_move(move[pos1][1]) == 'L' and first == '':
                first = move[pos1][1][0]
            if def_move(move[pos1][1]) == 'L':
                last = move[pos1][1][0]
                pos_last = pos1
            pos1 = pos1 + 1

        for trans in transitions:
            if trans.name == move[pos_start][0][1]:
                for tr in transitions:
                    if tr.label in sub:
                        if tr.label == first and tr.name[:1] == "s":
                            for place in places:
                                for arc in place.out_arcs:
                                    if arc.target.name == tr.name:
                                        trovato = False
                                        for ar in place.in_arcs:
                                            if ar.source.name == trans.name:
                                                trovato = True
                                                print("Arc:1 ", trans.label, trans.name, "-->", place,
                                                      " already existent")
                                                break
                                        if trovato:
                                            continue
                                        else:
                                            utils.add_arc_from_to(trans, place, net)
                                            print("Added: ", trans.label, trans.name, " --> ", place)
                                            added = added + 1

                    elif tr.label == first and tr.name[:1] == "n":
                        for place in places:
                            for arc in place.out_arcs:
                                if arc.target.name == tr.name:
                                    trovato = False
                                    for ar in place.in_arcs:
                                        if ar.source.name == trans.name:
                                            trovato = True
                                            print("Arc:1 ", trans.label, trans.name, "-->", place,
                                                  " already existent")
                                            break
                                    if trovato:
                                        continue
                                    else:
                                        utils.add_arc_from_to(trans, place, net)
                                        print("Added: ", trans.label, trans.name, " --> ", place)
                                        added = added + 1

            if trans.name == move[pos_last + 1][0][1]:
                for tr in transitions:
                    if tr.label in sub:
                        if tr.label == last and tr.name[:1] == "s":
                            for place in places:
                                for arc in place.in_arcs:
                                    if arc.source.name == tr.name:
                                        trovato2 = False
                                        for ar in place.out_arcs:
                                            if ar.target.name == trans.name:
                                                trovato2 = True
                                                print("Arc: ", place, "-->", trans.label, trans.name, " already existent")
                                                break
                                        if trovato2:
                                            continue
                                        else:
                                            utils.add_arc_from_to(place, trans, net)
                                            print("Added: ", place, " --> ", trans.label, trans.name)
                                            added = added + 1

                    elif tr.label == last and tr.name[:1] == "n":
                        for place in places:
                            for arc in place.in_arcs:
                                if arc.source.name == tr.name:
                                    trovato2 = False
                                    for ar in place.out_arcs:
                                        if ar.target.name == trans.name:
                                            trovato2 = True
                                            print("Arc: ", place, "-->", trans.label, trans.name, " already existent")
                                            break
                                    if trovato2:
                                        continue
                                    else:
                                        utils.add_arc_from_to(place, trans, net)
                                        print("Added: ", place, " --> ", trans.label, trans.name)
                                        added = added + 1

        if added == 0:
            print("The sub is perfectly fitting!")
            return 'U'
        else:
            # visualizza rete
            parameters = {petrinet_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "jpg"}
            gvz = petrinet_visualizer.apply(net, initial_marking, final_marking, parameters=parameters)
            petrinet_visualizer.view(gvz)
            return 'UA'
    else:
        print("The sub was not followed in the alignment!")
        return 'UNA'


"""Computes Precision, Fitness, Generalization and Simplicity w.r.t. an Event Log composed by graphs in which the sub occurs
INPUT: -graph_list: list of graphs in which the sub occurs
       -log: Event Log
       -dict_trace: dictionary with pairs idTrace:numTrace
       -net: the net model
       -initial_marking: initial marking of the model
       -final_marking: final marking of the model 
"""


def valutazione_rete(graph_list, log, dict_trace, net, initial_marking, final_marking, pattern, sub):
    new_eventlog = EventLog()
    for graph in graph_list:
        traccia = search_trace(log, dict_trace, graph)
        new_eventlog.append(traccia)

    # xes_exporter.apply(new_eventlog,'testlog.xes')

    fitness = replay_evaluator.apply(new_eventlog, net, initial_marking, final_marking,
                                     variant=replay_evaluator.Variants.ALIGNMENT_BASED)
    write_outputfile("Fitness:  " + str(fitness), pattern, sub, "a")
    # print("Fitness: ", fitness)
    precision = precision_evaluator.apply(new_eventlog, net, initial_marking, final_marking,
                                          variant=precision_evaluator.Variants.ALIGN_ETCONFORMANCE)
    write_outputfile("Precision:  " + str(precision), pattern, sub, "a")
    # print("Precision: ", precision)
    generalization = generalization_evaluator.apply(new_eventlog, net, initial_marking, final_marking)
    write_outputfile("Generalization:  " + str(generalization), pattern, sub, "a")
    # print("Generalization: ", generalization)
    simplicity = simplicity_evaluator.apply(net)
    write_outputfile("Simplicity:  " + str(simplicity), pattern, sub, "a")
    # print("Simplicity: ", simplicity)


"""Computes Precision, Fitness, Generalization and Simplicity w.r.t. a complete Event Log
INPUT: -log: Event Log
       -net: the net model
       -initial_marking: initial marking of the model
       -final_marking: final marking of the model 
"""

def valutazione_rete_logcompleto(log, net, initial_marking, final_marking, pattern, sub):
    fitness = replay_evaluator.apply(log, net, initial_marking, final_marking,
                                     variant=replay_evaluator.Variants.ALIGNMENT_BASED)

    write_outputfile("Fitness:  " + str(fitness), pattern, sub, "a")
    #print("Fitness: ", fitness)
    precision = precision_evaluator.apply(log, net, initial_marking, final_marking,
                                          variant=precision_evaluator.Variants.ALIGN_ETCONFORMANCE)

    write_outputfile("Precision:  " + str(precision), pattern, sub, "a")
    #print("Precision: ", precision)
    generalization = generalization_evaluator.apply(log, net, initial_marking, final_marking)

    write_outputfile("Generalization:  " + str(generalization), pattern, sub, "a")
    #print("Generalization: ", generalization)
    simplicity = simplicity_evaluator.apply(net)

    write_outputfile("Simplicity:  " + str(simplicity), pattern, sub, "a")
    #print("Simplicity: ", simplicity)


""" The function shows a Petri net
INPUT: -log: Event Log
       -net: the model net
       -initial_marking: initial marking of the model
       -final_marking: final marking of the model
"""


def visualizza_rete(log, net, im, fm):
    parameters = {petrinet_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "jpg", "debug": True}
    gvz = token_decoration_frequency.apply(net, im, fm, parameters=parameters)
    petrinet_visualizer.view(gvz)


""" The function shows a Petri net with performances
INPUT: -log: Event Log
       -net: the model net
       -initial_marking: initial marking of the model
       -final_marking: final marking of the model
"""

def visualizza_rete_performance(log, net, im, fm):
    agg_statistics = token_decoration_frequency.get_decorations(log, net, im, fm)
    parameters = {petrinet_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "jpg", "debug": True}
    gvz = token_decoration_frequency.apply(net, im, fm, aggregated_statistics=agg_statistics, parameters=parameters)
    # gvz = petrinet_visualizer.apply(net, initial_marking, final_marking, parameters=parameters)
    petrinet_visualizer.view(gvz)


""" The function exports an event log with the traces in which the sub occurs
INPUT: -graph_list: a list of graphs in which the sub occurs
       -log:  Event Log
       -dict_trace: dictionary with pairs idTrace:numTrace
       -sub: the number of the sub
"""


def export_eventlog_test(graph_list, log, dict_trace, sub):
    new_eventlog = EventLog()
    for gra in graph_list:
        tra = search_trace(log, dict_trace, gra)
        new_eventlog.append(tra)

    xes_exporter.apply(new_eventlog, '../testlog_' + sub + '.xes')


""" The functions performs the alignment of each trace in which the sub occurs
INPUT: -graph_list: a list of graphs in which the sub occurs
       -log:  Event Log
       -dict_trace: dictionary with pairs idTrace:numTrace
       -net: the net model
       -initial_marking: initial marking of the model
       -final_marking: final marking of the model 
"""


def all_alignment(graph_list, log, dict_trace, net, initial_marking, final_marking):
    print("Alignment of all traces in which the following sub occurs: ")
    for graph in graph_list:
        traccia = search_trace(log, dict_trace, graph)
        new_eventlog = EventLog()
        new_eventlog.append(traccia)

        align = alignment.apply_log(new_eventlog, net, initial_marking, final_marking)
        print("New Alignment " + traccia.attributes['concept:name'] + ": ", align)


""" The function cut the input graph to write it in the graph+n+.g file that can be passed to the tool gm
INPUT: -pattern: the folder containing files
       -graph: the graph name
       -subnumber: the number of the sub
RETURN: -n_sub: the graph part containing the sub to write on the file
"""


def graph_sub(pattern, graph, sub_number):
    a = split_subgraph(pattern + "/graphs/" + graph + ".g")
    sub = list(flatten(a))

    # esegue sgiso e ritorna la sub con i nodi rispetto al grafo
    subgraph = find_instances(sub_number, graph, pattern)

    # ritorna i nodi di inizio e fine sub
    start, end, sub_label = startend_node(subgraph)

    n_sub = []

    for x in range(len(sub)):
        if sub[x] == 'v':
            if int(sub[x + 1]) >= int(minimo_lista(start)) and int(sub[x + 1]) <= massimo_lista(end):
                n_sub.append(sub[x])
                n_sub.append(sub[x + 1])
                n_sub.append(sub[x + 2])
        elif sub[x] == 'd' or sub[x] == 'e':
            if int(minimo_lista(start)) <= int(sub[x + 1]) <= massimo_lista(end) and int(
                    minimo_lista(start)) <= int(sub[x + 2]) <= massimo_lista(end):
                n_sub.append(sub[x])
                n_sub.append(sub[x + 1])
                n_sub.append(sub[x + 2])
                n_sub.append(sub[x + 3])
    return n_sub


""" The function runs the gm tool to calculate the matching cost between the two input graphs
INPUT: -graph1: name of the first graph
       -graph1: name of the second graph
        - sub_number: the number of the sub
RETURN: -float(sub2[3]): Matching Cost
"""


def graph_matching(pattern, graph1, graph2, sub_number):
    secondgraph = graph_sub(pattern, graph2, sub_number)
    write_graphfile(secondgraph, "2", pattern)

    if graph1 == 'sub':
        out = subprocess.Popen([pattern + '/gm',
                                pattern + '/graphsub.g',
                                pattern + '/graph2.g'],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        sub = stdout.decode("utf-8")
        sub2 = sub.split()
    else:
        firstgraph = graph_sub(pattern, graph1, sub_number)
        write_graphfile(firstgraph, "1", pattern)
        out = subprocess.Popen([pattern + 'gm',
                                pattern + 'graph1.g',
                                pattern + 'graph2.g'],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        sub = stdout.decode("utf-8")
        sub2 = sub.split()

    return float(sub2[3])


""" The functions return the graph with the smallest matching cost
INPUT: -pattern: the folder containing files
       -graph: the graph name
       -graph_list: list of graphs in which the sub occurs
       -sub_number: the sub number
RETURN: -mingraph: list of graphs with the smallest cost
        -mincost: the smallest cost
"""


def graph_choice(pattern, graph, graph_list, sub_number):
    mincost = graph_matching(pattern, graph, graph_list[0], sub_number)
    mingraph = []
    for x in graph_list:
        cost = graph_matching(pattern, graph, x, sub_number)
        if cost < mincost:
            mincost = cost
            mingraph = []
            mingraph.append(x)
        elif cost == mincost:
            mingraph.append(x)

    return mingraph, mincost


""" The function creates the dictionaty with the ranking of the graphs matching the sub, ordered by increasing cost
INPUT: -pattern: the folder containing the files
       -graph: the graph name
       -graph_list: list of graphs in which the sub occurs
       -sub_number: the sub number
RETURN: -dict: dictionary with the ranking of the graphs based on the matching cost
"""


def create_dict_graph(pattern, graph, graph_list, sub_number):
    bar = IncrementalBar('Create dict_graph: ', max=len(graph_list))
    dict = {}
    i = 1
    list = []
    for x in graph_list:
        list.append(x)
    while len(list) != 0:
        min_graph, cost = graph_choice(pattern, graph, list, sub_number)
        for y in min_graph:
            bar.next()
            list.remove(y)
            dict[i] = (y, cost)
            i = i + 1
    bar.finish()

    return dict


""" The functions returns the graph with the smallest matching cost
INPUT: -graph: the graph name
       -graph_dict: dictionary including the output of create_dict_graph
       -log: Event Log
       -dict_trace: dictionary with pairs 'numTrace':'idTrace'
       -start_name: name of the start transition
       -end_name: name of the end transition
       -net: the net model
       -initial_marking: initial marking of the model
       -final_marking: final marking finale of the model
       -sub: list of the labels of the transitions in the sub
"""


def second_repairing(graph, graph_dict, log, dict_trace, start_name, end_name, net, initial_marking, final_marking,
                     sub_label, nrep, pattern, sub):
    usate = []
    non_usate = []
    for x in range(2, len(graph_dict)):
        if graph_dict[x][0] != graph and int(graph_dict[x][1]) != 0:
            non_usate.append(graph_dict[x][0])
    non_funzionanti = []
    list_rete1 = []
    i = 2
    rip = 0
    for y in range(2, len(graph_dict)):
        if (int(graph_dict[y][1]) > 0):
            rip = rip + 1
            gr = graph_dict[y][0]
            write_outputfile(str(gr) + " " + str(
                graph_dict[y][1]) + " ##############################################################################",
                             pattern, sub, "a")
            # print(gr, graph_dict[y][1], "##############################################################################")
            tr = search_trace(log, dict_trace, gr)
            # if str(gr) == 'graph1122':
            # print(gr)
            if list_rete1 == []:
                result = first_postrepairing_algorithm(tr, start_name, end_name, net, initial_marking, final_marking,
                                                       sub_label, pattern, sub)
                if type(result) == type([]):
                    # visualizza_rete_performance(log, result[0], result[1], result[2])
                    write_outputfile("\nEvaluation repaired net " + str(i) + " :", pattern, sub, "a")
                    # print("\nValutazione rete riparata " + str(i) + " :")
                    # valutazione_rete(new_graph_list, log, dict_trace, result[0], result[1], result[2], pattern, sub)
                    valutazione_rete_logcompleto(log, result[0], result[1], result[2], pattern, sub)
                    # visualizza_rete_performance(log, result[0], result[1], result[2])
                    list_rete1 = [result[0], result[1], result[2]]
                    i = i + 1
            else:
                result = first_postrepairing_algorithm(tr, start_name, end_name, list_rete1[0], list_rete1[1],
                                                       list_rete1[2], sub_label, pattern, sub)
                if type(result) == type([]):
                    # if i > 32: #da togliere
                    # visualizza_rete_performance(log, result[0], result[1], result[2])
                    write_outputfile("\nEvaluation repaired net " + str(i) + " :", pattern, sub, "a")
                    # print("\nValutazione rete riparata " + str(i) + " :")
                    # valutazione_rete(new_graph_list, log, dict_trace, result[0], result[1], result[2], pattern, sub)
                    valutazione_rete_logcompleto(log, result[0], result[1], result[2], pattern, sub)
                    # visualizza_rete_performance(log, result[0], result[1], result[2])
                    list_rete1 = [result[0], result[1], result[2]]
                    i = i + 1

            if result == 'UNA':
                non_funzionanti.append(gr)
                non_usate.remove(gr)
                write_outputfile("Traces in which the sub was not followed:  " + str(len(non_funzionanti)), pattern, sub, "a")
                # print("Non funzionanti: ", len(non_funzionanti))
                write_outputfile("Used:  " + str(len(usate)), pattern, sub, "a")
                # print("Usate: ", len(usate))
                write_outputfile("Not used:  " + str(len(non_usate)), pattern, sub, "a")
                # print("Non usate: ", len(non_usate))
            elif result == 'UNG':
                non_funzionanti.append(gr)
                non_usate.remove(gr)
                write_outputfile("The " + str(tr.attributes['concept:name']) + " was ignored! ", pattern, sub, "a")
                # print("La", tr.attributes['concept:name'], "e stata ignorata")
                write_outputfile("Traces in which the sub was not followed:  " + str(len(non_funzionanti)), pattern, sub, "a")
                # print("Non funzionanti: ", len(non_funzionanti))
                write_outputfile("Used:  " + str(len(usate)), pattern, sub, "a")
                # print("Usate: ", len(usate))
                write_outputfile("Not used:  " + str(len(non_usate)), pattern, sub, "a")
                # print("Non usate: ", len(non_usate))
            elif result == 'U':
                non_usate.remove(gr)
                write_outputfile("Traces in which the sub was not followed:  " + str(len(non_funzionanti)), pattern, sub, "a")
                # print("Non funzionanti: ", len(non_funzionanti))
                write_outputfile("Used:  " + str(len(usate)), pattern, sub, "a")
                # print("Usate: ", len(usate))
                write_outputfile("Not used:  " + str(len(non_usate)), pattern, sub, "a")
                # print("Non usate: ", len(non_usate))
            else:
                usate.append(gr)
                non_usate.remove(gr)
                write_outputfile("Traces in which the sub was not followed:  " + str(len(non_funzionanti)), pattern, sub, "a")
                # print("Non funzionanti: ", len(non_funzionanti))
                write_outputfile("Used:  " + str(len(usate)), pattern, sub, "a")
                # print("Usate: ", len(usate))
                write_outputfile("Not used:  " + str(len(non_usate)), pattern, sub, "a")
                # print("Non usate: ", len(non_usate))

            if len(usate) == nrep:
                write_outputfile("\n" + str(nrep) + " repairments have been done!", pattern, sub, "a")
                # print("\nSono state effettuate " + str(nrep) + " riparazioni!")
                break
    if rip == 0:
        write_outputfile(
            "\nAll traces have GM = 0 w.r.t. the sub: no further repairments are needed!", pattern,
            sub, "a")
    if list_rete1 != []:
        return list_rete1, non_funzionanti
    else:
        rete = [net, initial_marking, final_marking]
        return rete, non_funzionanti


def main(pattern, dataset, numsub):
    debug = False

    # Eventlog
    log = xes_importer.apply(pattern + "/"+ dataset+ '.xes')
    # Model
    net, initial_marking, final_marking = pnml_importer.apply(pattern +"/"+ dataset + '_petriNet.pnml')
    # net, initial_marking, final_marking = pnml_importer.apply(pattern + '/reti_Fahland/repaired_'+str(x)+'.pnml')

    # given the pattern number, return the list of subs
    # lista = list_sub_pattern(pattern + dataset + "_new_patterns_filtered.subs", 2)
    # print("Pattern: ", lista)
    # write_outputfile("Pattern:  " + str(lista), pattern, sub, "w")

    sub = numsub  # lista[0] if we take the sub from the list of patterns
    # print("Sub Selected: ", sub)
    write_outputfile("Sub Selected:  " + str(sub), pattern, sub, "w")

    # dict 'numTrace':'traceId'
    dict_trace = create_dict_trace(dataset)
    # create file subelements.txt with extended subs (TODO: decomment if already created)
    create_subelements_file(dataset, pattern)

    # given a sub, returns the list of graphs in which the sub occurs
    graph_list = list_graph_occurence(pattern + "/"+ dataset + "_table2_on_file.csv", sub)
    new_graph_list = check_graphlist(graph_list, sub, pattern)
    write_outputfile("Number of graphs in which the sub occurs: " + str(len(new_graph_list)), pattern, sub, "a")
    dict_graph = create_dict_graph(pattern, "sub", new_graph_list, sub)
    graph = dict_graph[1][0]
    # print("Graph Selected: ", graph, " Matching Cost: ", dict_graph[1][1])
    write_outputfile("Graph Selected:  " + str(graph) + "  Matching Cost:  " + str(dict_graph[1][1]), pattern, sub, "a")

    write_outputfile("\nEvaluation initial net:", pattern, sub, "a")
    #print("\nValutazione rete sub_" + str(x) + ":")
    # evaluation of the log composed by only traces in which the sub occurs
    # valutazione_rete(new_graph_list, log, dict_trace, net, initial_marking, final_marking, pattern, sub)
    # evaluation on the complete log
    valutazione_rete_logcompleto(log, net, initial_marking, final_marking, pattern, sub)
    # visualization of the net
    visualizza_rete_performance(log, net, initial_marking, final_marking)

    # executes sgiso and returns the sub with the nodes w.r.t the graph
    subgraph = find_instances(sub, graph, pattern)
    # print("Subgraph: ", subgraph)
    write_outputfile("Subgraph:  " + str(subgraph), pattern, sub, "a")

    # create the event log with the traces in which the sub occurs
    export_eventlog_test(graph_list, log, dict_trace, sub)

    # returns the start and end nodes
    start, end, sub_label = startend_node(subgraph)
    # print("Sub iniziale: ", sub_label)
    write_outputfile("Initial sub:  " + str(sub_label), pattern, sub, "a")

    # Trace
    trace = search_trace(log, dict_trace, graph)
    # print('Trace: ', trace.attributes['concept:name'])
    write_outputfile('Trace:  ' + str(trace.attributes['concept:name']), pattern, sub, "a")

    # Alignment
    text = search_alignment(pattern, dict_trace, graph)
    # print('Alignment: ' + text)
    write_outputfile('Alignment: ' + str(text), pattern, sub, "a")

    # Pre-filtering of the sub already present in the model
    new_subgrap = start_pre_process_repairing(start, text, subgraph)
    new_subgraph = end_pre_process_repairing(end, text, new_subgrap)
    # print("Subgraph semplificata: ", new_subgraph)
    write_outputfile("Simplified subgraph:  " + str(new_subgraph), pattern, sub, "a")

    # returns the start and end nodes
    start, end, sub_label = startend_node(new_subgraph)
    # print("Sub semplificata: ", sub_label)
    write_outputfile("Simplified sub:  " + str(sub_label), pattern, sub, "a")

    # print("Start: ", minimo_lista(start))
    write_outputfile("Start:  " + str(minimo_lista(start)), pattern, sub, "a")
    # returns the places where to attach the start nodes
    reached_marking_start = dirk_marking_start(dataset, start, text, trace, pattern, sub)
    # print("Reached Marking: ", reached_marking_start)
    write_outputfile("Reached Marking:  " + str(reached_marking_start), pattern, sub, "a")

    # print("End: ", massimo_lista(end))
    write_outputfile("End:  " + str(massimo_lista(end)), pattern, sub, "a")
    # returns the place where to attach the end nodes
    reached_marking_end = dirk_marking_end(dataset, end, text, trace, pattern, sub)
    # print("Reached Marking: ", reached_marking_end)
    write_outputfile("Reached Marking:  " + str(reached_marking_end), pattern, sub, "a")

    # tempo1 = timer()
    # repair the model with the subgraph
    start_end_name, net_repaired = repairing(new_subgraph, net, initial_marking, final_marking, start, end,
                                             reached_marking_start, reached_marking_end, pattern, sub)
    start_name = start_end_name[0]
    end_name = start_end_name[1]

    write_outputfile("\nEvaluation repaired net:", pattern, sub, "a")
    # print("\nEvaluation of the repaired net:")
    # Evaluation on the log only including traces with the sub
    # valutazione_rete(new_graph_list, log, dict_trace, net_repaired, initial_marking, final_marking, pattern, sub)
    # Evauation on the complete log
    valutazione_rete_logcompleto(log, net_repaired, initial_marking, final_marking, pattern, sub)
    # Visualization of the net
    visualizza_rete_performance(log, net, initial_marking, final_marking)

    # repairs the model a second time with one of the two algorithms
    #CHANGE LAURA 13/07/2021: we only want to repair once, for now.
    rete = [net_repaired, initial_marking, final_marking]                                                                                                                 
    #rete, non_funzionanti = second_repairing(graph, dict_graph, log, dict_trace, start_name, end_name, net_repaired,initial_marking, final_marking, sub_label, 20, pattern, sub)

    # EXECUTION TIME INSTRUCTIONS
    # tempo2 = timer()
    # print('\n\n', tempo2 - tempo1)
    # print('\n\n', tempo2 - tempo3)

    # show the net
    visualizza_rete_performance(log, rete[0], rete[1], rete[2])
    write_outputfile("\nValutazione rete riparata finale:", pattern, sub, "a")
    # print("\nValutazione rete riparata finale:")
    # evaluation on the log composed by traces in which the sub occurs
    # valutazione_rete(new_graph_list, log, dict_trace, net_repaired, initial_marking, final_marking)
    # evaluation on the complete log
    valutazione_rete_logcompleto(log, rete[0], rete[1], rete[2], pattern, sub)

    # export the pnml net
    pnml_exporter.apply(rete[0], rete[1], "../repaired_" + "Sub" + sub + "_petriNet.pnml", final_marking=rete[2])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Model Repair Supported by Frequent Anomalous Local Instance Graphs")
    #parser.add_argument("path", type=str,
      #                  help="Path della directory contenente: *_table2_on_file.csv | *_new_patterns_filtered.subs | rules_log.txt")
    parser.add_argument("datasetname", type=str, help="Name of the dataset to analyse")
    parser.add_argument("numsub", type=str, help="Number of the sub with which the model is to be repaired")
    args = parser.parse_args()
    main("../patterns_file", args.datasetname, args.numsub) #BPI2017Denied, testBank2000NoRandomNoise

    #main("../patterns_file/", "fineExp", "59")
