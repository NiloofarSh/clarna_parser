import os
from operator import itemgetter
cwd = os.getcwd()

def output_below_t(all_interactions_below_t,input_file_name, out, log):
    # Write in the output text file ".json.clarna.txt" and the log file ".log".
    #canonical_file_name = cwd + '/' + input_file_name + '_below_the_threshold.SS'
    #canonical = open(canonical_file_name, 'w')
    out.write('\n')

    # canonical pairs
    try:
        out.write('>canonical_pairs_below_the_threshold'+'\n')
        if all_interactions_below_t['canonical'] != {}:

            secondary_structure = {}
            for k, value in all_interactions_below_t['canonical'].items():
                sec_str = []
                for v in value:
                    sec_str.append(v[1])
                secondary_structure[k] = sec_str
            secondary_struc = []
            for k, v in secondary_structure.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([secondary_structure[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Canonical pairs below the threshold are not extracted!\n")

    # Other pairs
    try:
        out.write('>other_pairs_below_the_threshold' + '\n')
        if all_interactions_below_t['other_pairs'] != {}:
            other = {}
            for k, value in all_interactions_below_t['other_pairs'].items():
                other_str = []
                for v in value:
                    other_str.append(v[1])
                other[k] = other_str
            secondary_struc = []
            for k, v in other.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([other[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Other pairs below the threshold are not extracted!\n")

    # base-phosphate
    try:
        out.write('>base-phosphate_below_the_threshold'+'\n')
        if all_interactions_below_t['base_phosphate'] != {}:
            base = {}
            for k, value in all_interactions_below_t['base_phosphate'].items():
                base_str = []
                for v in value:
                    base_str.append(v[1])
                base[k] = base_str
            secondary_struc = []
            for k, v in base.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([base[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Base-phosphate below the threshold is not extracted!\n")

    # phosphate-base
    try:
        out.write('>phosphate-base_below_the_threshold' + '\n')
        if all_interactions_below_t['phosphate_base'] != {}:
            phosphate = {}
            for k, value in all_interactions_below_t['phosphate_base'].items():
                phosphate_str = []
                for v in value:
                    phosphate_str.append(v[1])
                phosphate[k] = phosphate_str
            secondary_struc = []
            for k, v in phosphate.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([phosphate[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Phosphate-base below the threshold is not extracted!\n")

    # stacking >>
    try:
        out.write('>stacking_>>_below_the_threshold'+'\n')
        if all_interactions_below_t['stacking_1'] != {}:
            stack_1 = {}
            for k, value in all_interactions_below_t['stacking_1'].items():
                stack_1_str = []
                for v in value:
                    stack_1_str.append(v[1])
                stack_1[k] = stack_1_str
            secondary_struc = []
            for k, v in stack_1.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([stack_1[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Stacking >> below the threshold is not extracted!\n")

    # stacking <<'
    try:
        out.write('>stacking_<<_below_the_threshold' + '\n')
        if all_interactions_below_t['stacking_2'] != {}:
            stack_2 = {}
            for k, value in all_interactions_below_t['stacking_2'].items():
                stack_2_str = []
                for v in value:
                    stack_2_str.append(v[1])
                stack_2[k] = stack_2_str
            secondary_struc = []
            for k, v in stack_2.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([stack_2[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Stacking << below the threshold is not extracted!\n")

    # stacking <>
    try:
        out.write('>stacking_<>_below_the_threshold'+'\n')
        if all_interactions_below_t['stacking_3'] != {}:
            stack_3 = {}
            for k, value in all_interactions_below_t['stacking_3'].items():
                stack_3_str = []
                for v in value:
                    stack_3_str.append(v[1])
                stack_3[k] = stack_3_str
            secondary_struc = []
            for k, v in stack_3.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([stack_3[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Stacking <> below the threshold is not extracted!\n")

    # stacking ><
    try:
        out.write('>stacking_><_below_the_threshold' + '\n')
        if all_interactions_below_t['stacking_4'] != {}:
            stack_4 = {}
            for k, value in all_interactions_below_t['stacking_4'].items():
                stack_4_str = []
                for v in value:
                    stack_4_str.append(v[1])
                stack_4[k] = stack_4_str
            secondary_struc = []
            for k, v in stack_4.items():
                baz = v.index('(')
                baste = v.index(')')
                secondary_struc.append([stack_4[k], baz, baste])
            sorted_sec = sorted(secondary_struc, key=itemgetter(1))
            for sec in range(len(sorted_sec)):
                for s in sorted_sec[sec][0]:
                    out.write(s)
                out.write('\n')
        else:
            out.write('None\n')
    except:
        out.write('None\n')
        if all_interactions_below_t['consensus'] == '':
            log.write("Notice: Stacking >< below the threshold is not extracted!\n")
