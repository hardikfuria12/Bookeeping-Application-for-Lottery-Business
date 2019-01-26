def main(ip1):
    entire_list = [100, 110, 166, 112, 113, 114, 115, 116, 117, 118,
		119, 200, 229, 220, 122, 277, 133, 224, 144, 226,
		155, 228, 300, 266, 177, 330, 188, 233, 199, 244,
		227, 255, 337, 338, 339, 448, 223, 288, 225, 299,
		335, 336, 355, 400, 366, 466, 377, 440, 388, 334,
		344, 499, 445, 446, 447, 556, 449, 477, 559, 488,
		399, 660, 599, 455, 500, 600, 557, 558, 577, 550,
		588, 688, 779, 699, 799, 880, 566, 800, 667, 668,
		669, 778, 788, 770, 889, 899, 700, 990, 900, 677,
		777, 444, 111, 888, 555, 222, 999, 666, 333, '000']

    entire_list=[str(x) for x in entire_list]
    from itertools import permutations
    ll=list(str(ip1))
    ll.extend(ll)
    perm=permutations(ll,3)
    main_op=""
    all_tickets=[]
    valid_tickets=[]
    for i in list(perm):
        a,b,c=i
        z=a+b+c
        if z in entire_list:
            valid_tickets.append(z)
    # print(valid_tickets)
    # print(len(valid_tickets))
    # 	main_op=main_op+z+"_"
    # main_op=main_op[:-1]
    valid_tickets=list(set(valid_tickets))

    print(len(valid_tickets))
    output_str = '_'.join(valid_tickets)
    print(output_str)
    return output_str

if __name__ == "__main__":
    main(123456789)



