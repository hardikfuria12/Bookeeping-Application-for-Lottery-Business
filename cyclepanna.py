def main(ip1):
    entire_list=[
                    128,129,120,130,140,123,124,125,126,127,
                    137,138,139,149,159,150,160,134,135,136,
                    146,147,148,158,168,169,179,170,180,145,
                    236,156,157,167,230,178,250,189,234,190,
                    245,237,238,239,249,240,269,260,270,235,
                    290,246,247,248,258,259,278,279,289,280,
                    380,345,256,257,267,268,340,350,360,370,
                    470,390,346,347,348,349,359,369,379,389,
                    489,480,490,356,357,358,368,378,450,460,
                    560,570,580,590,456,367,458,459,469,479,
                    579,589,670,680,690,457,467,468,478,569,
                    678,679,689,789,780,790,890,567,568,578,
                    100,110,166,112,113,114,115,116,117,118,
                    119,200,229,220,122,277,133,224,144,226,
                    155,228,300,266,177,330,188,233,199,244,
                    227,255,337,338,339,448,223,288,225,299,
                    335,336,355,400,366,466,377,440,388,334,
                    344,499,445,446,447,556,449,477,559,488,
                    399,660,599,455,500,600,557,558,577,550,
                    588,688,779,699,799,880,566,800,667,668,
                    669,778,788,770,889,899,700,990,900,677,
                    777,444,111,888,555,222,999,666,333,'000']

    ip1=str(ip1)
    l_ip1=list(ip1)
    op1='?'+l_ip1[0]+l_ip1[1]
    op2=l_ip1[0]+'?'+l_ip1[1]
    op3=l_ip1[0]+l_ip1[1]+'?'
    # print(len(entire_list))
    entire_list=[str(i) for i in entire_list]
    # print(entire_list)
    import fnmatch
    # filtered1 = fnmatch.filter(entire_list, '2?7')
    # filtered2 = fnmatch.filter(entire_list, '?27')
    # filtered3 = fnmatch.filter(entire_list, '27?')
    filtered1 = fnmatch.filter(entire_list, op1)
    filtered2 = fnmatch.filter(entire_list, op2)
    filtered3 = fnmatch.filter(entire_list, op3)
    filtered=[]
    filtered.extend(filtered1)
    filtered.extend(filtered2)
    filtered.extend(filtered3)
    # print(filtered)
    filtered=list(set(filtered))
    # print(filtered)
    output_str='_'.join(filtered)
    print(output_str)
    return output_str




if __name__=="__main__":
    main(69)
