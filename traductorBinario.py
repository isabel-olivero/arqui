hexatobin = {
    '0': "00000",
    '1': "00001",
    '2': "00010",
    '3': "00011",
    '4': "00100",
    '5': "00101",
    '6': "00110",
    '7': "00111",
    '8': "01000",
    '9': "01001",
    'A': "01010",
    'B': "01011",
    'C': "01100",
    'D': "01101",
    'E': "01110",
    'F': "01111"
}




MipsRHexa = {
   "20": "100000",
   "21":"100001",
   "24":"100100",
   "08":"001000",
    "25":"100101",
    "2a":"101010",
    "2b":"101011",
    "00":"000000",
    "02":"000010",
    "22":"100010",
    "23":"100011"
}

tipos = {
    "add": "R",
    "addi": "I",
    "addiu": "I",
    "addu": "R",
    "and": "R",
    "andi": "I",
    "beq": "I",
    "bne": "I",
    "j": "J",
    "jal": "J",
    "jr": "R",
    "lbu": "I",
    "lhu": "I",
    "ll": "I",
    "lui": "I",
    "lw": "I",
    "nor": "R",
    "or": "R",
    "ori": "I",
    "slt": "R",
    "sltiu": "I",
    "sltu": "R",
    "sll": "R",
    "srl": "R",
    "sb": "I",
    "sc": "I",
    "sh": "I",
    "sw": "I",
    "sub": "R",
    "subu": "R",
}
registros = {
    "$zero": "00000",
    "$at": "00001",
    "$v0": "00010",
    "$v1":"00011",
    "$a0": "00100",
    "$a1": "00101",
    "$a2": "00110",
    "$a3": "00111",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$s0": "10000",
    "$s1": "10001",
    "$s2": "10010",
    "$s3": "10011",
    "$s4": "10100",
    "$s5": "10101",
    "$s6": "10110",
    "$s7": "10111",
    "$t8": "11000",
    "$t9": "11001",
    "$k0": "11010",
    "$k1": "11011",
    "$gp": "11100",
    "$sp": "11101",
    "$fp": "11110",
    "$ra": "11111",
    "addi": "001000",
    "lw": "100011",
    "sw": "101011",
    "sub": "100010",
    "mult": "011000",
    "multu": "011001",
    "mfhi": "010000",
    "mflo": "010010",
    "div": "011010",
    "lui": "001111",
    "ori": "001101",
    "beq": "000100",
    "bne": "000101",
    "j": "000010",
    "jal": "000011",
    "jr": "001000",
    "slt": "101010",
    "addiu": "001000",
    "addu": "100001",
    "andi": "001100",
    "lbu": "100100",
    "lhu": "100101",
    "ll": "110000",
    "slti": "001010",
    "sltiu": "001011",
    "sltu": "101011",
    "sll": "000000",
    "srl": "000010",
    "sb": "101000",
    "sc": "111000",
    "sh": "101001",
    "subu": "100011",
    "and": "100100",
    "or": "100101",
    "nor": "100111",
    "divu": "011011"
}
rfunc ={
    "add":"20","addu":"21",
      "and":"24", "jr":"08",
      "nor":"27", "or":"25", 
      "slt":"2a","sltu":"2b",
      "sll":"00","srl":"02", 
      "sub":"22","subu":"23" }

    



def traduceMips (lista,tipos,registros, hexatobin, MipsRHexa,rfunc):
    ans = ""
    flag = False
    opcode = ""
    rs = ""
    rt = ""
    rd = ""
    shamt = ""
    funct = ""
    immediate = ""
    address = ""
    tipo = ""

    
    #se hace la traduccion del opcode segun el tipo
    if lista[0] in tipos:
        tipo = tipos[lista[0]]
    else:
        print("Tipo no encontrado")
    
    if tipo == "R":
        opcode = "000000"
    else:
        opcode = registros[lista[0]]

    #finaliza traduccion de opcode
        
    if tipo == "R":
        rd = registros[lista[1]]
        rs = registros[lista[2]]
        if lista[3] in registros:
            rt = registros[lista[3]]
        else:
            rt = registros[lista[2]]
            rs= "00000"

        f = rfunc[lista[0]]
        funct = MipsRHexa[f]


        if lista[0] == "sll":
            shamt = hexatobin[lista[3]]
        
        elif lista[0] == "srl":
            shamt = hexatobin[lista[4]]
        else:
            shamt = "00000"
        ans = opcode +" "+ rs +" " + rt +" " + rd +" "+ shamt +" "+ funct
        

    elif tipo == "I":
        rs = registros[lista[1]]
        rt = registros[lista[2]]
        immediate = bin(lista[3])#"00000000000" + hexatobin[lista[3]]
        ans = opcode +" "+ rs +" " + rt +" " + immediate

    elif tipo == "J":
        "pendiente"

    
    return ans
        
#a = traduceMips (["addi","$s1","$s1","2"],tipos,registros, hexatobin, MipsRHexa)
#print(a)


def operahexa(hexa, hexb):
    n1=int (hexa,16)
    n2=int(hexb,16)
    ans= hex(n1+n2)
    return ans

def transformaist(cadi):
    ignor={"(",")", ","," "}
    aux = ""
    for i in range(len(cadi)):
        if cadi[i] in ignor:
            a= "_"
        else:
            a=cadi[i]
        aux += a
   
    cadimod = aux.split("_")
    

    return cadimod


    
def funtipoi(funlista,registros):
    ans=""
    if tipos[funlista[0]] == "I":
        opcode = registros[funlista[0]]
        if (funlista[0] == 'lw') or (funlista[0] =="sw"):
            rt =registros[ funlista[1]]
            auxin = int(funlista[2])
            auxstr= bin(auxin) 
            immediate= str(auxstr)
            rs =registros[ funlista[3]]
        else:
            rt=registros[ funlista[1]]
            rs =registros[ funlista[2]]
            auxin = int(funlista[3])
            auxstr= bin(auxin)
            immediate= str(auxstr)
    ans= opcode+" "+rs+" "+rt+" "+immediate
    return ans
c=transformaist("lw $t0,100($t1)")
b= funtipoi(c,registros)
print(b)
     



        

           

        







