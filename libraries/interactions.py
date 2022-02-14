# Extract the "canonical pairs" from the json file.

def canonical_pairs(sorted_residue, content, threshold, log):
    total_canonical ={}
    canonical = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (((link["desc"] == 'WW_cis' and (link['n_type'] =='GC' or link['n_type'] =='CG' or link['n_type'] == 'AU' or link['n_type'] =='UA' or link['n_type'] =='GU' or link['n_type'] =='UG'))
                    or (link["desc"] == '?WW_cis' and (link['n_type'] =='GC' or link['n_type'] =='CG' or link['n_type'] == 'AU' or link['n_type'] =='UA' or link['n_type'] =='GU' or link['n_type'] =='UG'))) \
                    and link['source']< link['target']):
                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] \
                            and any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):

                        if int(content['nodes'][link['source']]['id'][1:])< int(content['nodes'][link['target']]['id'][1:]):
                            canonical[counter] = [sorted_residue[r], '(']
                        else:
                            canonical[counter] = [sorted_residue[r], ')']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] \
                            and any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):

                        if int(content['nodes'][link['target']]['id'][1:]) > int(content['nodes'][link['source']]['id'][1:]):
                            canonical[counter] = [sorted_residue[r], ')']
                        else:
                            canonical[counter] = [sorted_residue[r], '(']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) \
                            and sorted_residue[r][1][0]['id'] != content['nodes'][link['source']]['id']\
                            and sorted_residue[r][1][0]['id'] != content['nodes'][link['target']]['id']:
                        canonical[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v =[]
                for k, v in canonical.items():
                    total_v.append(v)
                total_canonical[counter1]= total_v

    #sorted_total_canonical[k] = sorted(value.items(), key=lambda item: item[1][0][0])
    log.write('Canonical pairs is extracting... ')
    return total_canonical

#*******************************************************
# Extract the "Other pairs" from the json file.
def other_pairs(sorted_residue, content, threshold, log):
    total_other_pairs = {}
    other = {}
    counter1 = 0

    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and link['source']< link['target'] and (link["desc"] == 'WW_tran'
                    or link["desc"] == 'WH_cis' or link["desc"] == 'HW_cis' or link["desc"] == 'WH_tran'
                    or link["desc"] == 'HW_tran' or link["desc"] == 'WS_cis' or link["desc"] == 'SW_cis'
                    or link["desc"] == 'WS_tran' or link["desc"] == 'SW_tran' or link["desc"] == 'HH_cis'
                    or link["desc"] == 'HH_tran' or link["desc"] == 'HS_cis' or link["desc"] == 'SH_cis'
                    or link["desc"] == 'HS_tran' or link["desc"] == 'SH_tran' or link["desc"] == 'SS_cis'
                    or link["desc"] == 'SS_tran' or link["desc"] == '?WW_tran' or link["desc"] == '?WH_cis'
                    or link["desc"] == '?HW_cis' or link["desc"] == '?WH_tran' or link["desc"] == '?HW_tran'
                    or link["desc"] == '?WS_cis' or link["desc"] == '?SW_cis' or link["desc"] == '?WS_tran'
                    or link["desc"] == '?SW_tran' or link["desc"] == '?HH_cis' or link["desc"] == '?HH_tran'
                    or link["desc"] == '?HS_cis' or link["desc"] == '?SH_cis' or link["desc"] == '?HS_tran'
                    or link["desc"] == '?SH_tran' or link["desc"] == '?SS_cis' or link["desc"] == '?SS_tran'
                    or
                    ((link["desc"] == 'WW_cis' and (link['n_type'] == 'CC' or link['n_type'] == 'GG'
                    or link['n_type'] == 'UU' or link['n_type'] == 'AA' or link['n_type'] == 'AG'
                    or link['n_type'] == 'GA')) or (link["desc"] == '?WW_cis' and (link['n_type'] == 'AC'
                    or link['n_type'] == 'CA' or link['n_type'] == 'CG' or link['n_type'] == 'GC'
                    or link['n_type'] == 'CU' or link['n_type'] == 'UC')))):

                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) < int(
                                content['nodes'][link['target']]['id'][1:]):
                            other[counter] = [sorted_residue[r], '(']
                        else:
                            other[counter] = [sorted_residue[r], ')']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) > int(
                                content['nodes'][link['source']]['id'][1:]):
                            other[counter] = [sorted_residue[r], ')']
                        else:
                            other[counter] = [sorted_residue[r], '(']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        other[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                for k, v in other.items():
                    total_v.append(v)
                total_other_pairs[counter1] = total_v

    log.write('Other pairs is extracting... ')
    return total_other_pairs


#*******************************************************
# Extract the "base-phosphate" from the json file.
def base_phosphate(sorted_residue, content, threshold, log):
    total_base_phosphate = {}
    base_phosphate = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (link["desc"] == 'H_0BPh' or link["desc"] == 'S_1BPh'
                    or link["desc"] == 'SW_2BPh' or link["desc"] == 'W_345BPh' or link["desc"] == 'W_6BPh'
                    or link["desc"] == 'H_789BPh' or link["desc"] == '?H_0BPh' or link["desc"] == '?S_1BPh'
                    or link["desc"] == '?SW_2BPh' or link["desc"] == '?W_345BPh' or link["desc"] == '?W_6BPh'
                    or link["desc"] == '?H_789BPh'):

                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) < int(
                                content['nodes'][link['target']]['id'][1:]):
                            base_phosphate[counter] = [sorted_residue[r], '(']
                        else:
                            base_phosphate[counter] = [sorted_residue[r], '.']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) > int(
                                content['nodes'][link['source']]['id'][1:]):
                            base_phosphate[counter] = [sorted_residue[r], ')']
                        else:
                            base_phosphate[counter] = [sorted_residue[r], '.']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        base_phosphate[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                dot = []
                for k, v in base_phosphate.items():
                    dot.append(v[1])
                    total_v.append(v)
                if all(i == '.' for i in dot) == False:
                    total_base_phosphate[counter1] = total_v

    log.write('Base-phosphate is extracting... ')
    return total_base_phosphate

#*******************************************************
# Extract the "phosphate-base" from the json file.
def phosphate_base(sorted_residue, content, threshold, log):
    total_phosphate_base = {}
    phosphate_base = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (link["desc"] == 'H_0BPh' or link["desc"] == 'S_1BPh'
                    or link["desc"] == 'SW_2BPh' or link["desc"] == 'W_345BPh' or link["desc"] == 'W_6BPh'
                    or link["desc"] == 'H_789BPh' or link["desc"] == '?H_0BPh' or link["desc"] == '?S_1BPh'
                    or link["desc"] == '?SW_2BPh' or link["desc"] == '?W_345BPh' or link["desc"] == '?W_6BPh'
                    or link["desc"] == '?H_789BPh'):

                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) > int(
                                content['nodes'][link['target']]['id'][1:]):
                            phosphate_base[counter] = [sorted_residue[r], ')']
                        else:
                            phosphate_base[counter] = [sorted_residue[r], '.']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) < int(
                                content['nodes'][link['source']]['id'][1:]):
                            phosphate_base[counter] = [sorted_residue[r], '(']
                        else:
                            phosphate_base[counter] = [sorted_residue[r], '.']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        phosphate_base[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                dot = []
                for k, v in phosphate_base.items():
                    dot.append(v[1])
                    total_v.append(v)
                if all(i == '.' for i in dot) == False:
                    total_phosphate_base[counter1] = total_v

    log.write('Phosphate-base is extracting... ')
    return total_phosphate_base


#*******************************************************
def stacking_1(sorted_residue, content, threshold, log):
    total_stacking_1 = {}
    stack_1 = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (link["desc"] == '>>' or link["desc"] == '?>>') and link['source']< link['target']:
                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) < int(
                                content['nodes'][link['target']]['id'][1:]):
                            stack_1[counter] = [sorted_residue[r], '(']
                        else:
                            stack_1[counter] = [sorted_residue[r], ')']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) > int(
                                content['nodes'][link['source']]['id'][1:]):
                            stack_1[counter] = [sorted_residue[r], ')']
                        else:
                            stack_1[counter] = [sorted_residue[r], '(']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        stack_1[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                for k, v in stack_1.items():
                    total_v.append(v)
                total_stacking_1[counter1] = total_v

    log.write('Stacking >> is extracting... ')
    return total_stacking_1

#*******************************************************
# Extract the "stacking <<" from the json file.
def stacking_2(sorted_residue, content, threshold, log):
    total_stacking_2 = {}
    stacking_2 = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (link["desc"] == '<<' or link["desc"] == '?<<') and link['source']< link['target']:
                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) < int(
                                content['nodes'][link['target']]['id'][1:]):
                            stacking_2[counter] = [sorted_residue[r], '(']
                        else:
                            stacking_2[counter] = [sorted_residue[r], ')']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) > int(
                                content['nodes'][link['source']]['id'][1:]):
                            stacking_2[counter] = [sorted_residue[r], ')']
                        else:
                            stacking_2[counter] = [sorted_residue[r], '(']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        stacking_2[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                for k, v in stacking_2.items():
                    total_v.append(v)
                total_stacking_2[counter1] = total_v

    log.write('Stacking >> is extracting... ')
    return total_stacking_2

#*******************************************************
# Extract the "stacking <>" from the json file.
def stacking_3(sorted_residue, content, threshold, log):
    total_stacking_3 = {}
    stacking_3 = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (link["desc"] == '<>' or link["desc"] == '?<>') and link['source']< link['target']:
                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) < int(
                                content['nodes'][link['target']]['id'][1:]):
                            stacking_3[counter] = [sorted_residue[r], '(']
                        else:
                            stacking_3[counter] = [sorted_residue[r], ')']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) > int(
                                content['nodes'][link['source']]['id'][1:]):
                            stacking_3[counter] = [sorted_residue[r], ')']
                        else:
                            stacking_3[counter] = [sorted_residue[r], '(']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        stacking_3[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                for k, v in stacking_3.items():
                    total_v.append(v)
                total_stacking_3[counter1] = total_v

    log.write('Stacking <> is extracting... ')
    return total_stacking_3

#*******************************************************
# Extract the "stacking ><" from the json file.
def stacking_4(sorted_residue, content, threshold, log):
    total_stacking_4 = {}
    stacking_4 = {}
    counter1 = 0
    for link in content['links']:
        if "desc" in link:
            if float(link['weight']) >= threshold and (link["desc"] == '><' or link["desc"] == '?><') and link['source']< link['target']:
                counter = 0
                for r in range(len(sorted_residue)):
                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['source']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['source']]['id'][1:]) < int(
                                content['nodes'][link['target']]['id'][1:]):
                            stacking_4[counter] = [sorted_residue[r], '(']
                        else:
                            stacking_4[counter] = [sorted_residue[r], ')']

                    if sorted_residue[r][1][0]['id'] == content['nodes'][link['target']]['id'] and any(
                            c in 'AUGC' for c in sorted_residue[r][1][0]['resname']):
                        if int(content['nodes'][link['target']]['id'][1:]) > int(
                                content['nodes'][link['source']]['id'][1:]):
                            stacking_4[counter] = [sorted_residue[r], ')']
                        else:
                            stacking_4[counter] = [sorted_residue[r], '(']

                    elif any(c in 'AUGC' for c in sorted_residue[r][1][0]['resname']) and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['source']]['id'] and sorted_residue[r][1][0]['id'] != \
                            content['nodes'][link['target']]['id']:
                        stacking_4[counter] = [sorted_residue[r], '.']
                    counter += 1
                counter1 += 1

                # total canonicals :D
                total_v = []
                for k, v in stacking_4.items():
                    total_v.append(v)
                total_stacking_4[counter1] = total_v

    log.write('Stacking >< is extracting... ')
    return total_stacking_4

