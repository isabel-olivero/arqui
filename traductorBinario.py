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

bintohexa = {
    "0000": '0',
    "0001": '1',
    "0010": '2',
    "0011": '3',
    "0100": '4',
    "0101": '5',
    "0110": '6',
    "0111": '7',
    "1000": '8',
    "1001": '9',
    "1010": 'A',
    "1011": 'B',
    "1100": 'C',
    "1101": 'D',
    "1110": 'E',
    "1111": 'F'
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

binregistro= {
    "00000": "$zero",
    "00001": "$at",
    "00010": "$v0",
    "00011": "$v1",
    "00100": "$a0",
    "00101": "$a1",
    "00110": "$a2",
    "00111": "$a3",
    "01000": "$t0",
    "01001": "$t1",
    "01010": "$t2",
    "01011": "$t3",
    "01100": "$t4",
    "01101": "$t5",
    "01110": "$t6",
    "01111": "$t7",
    "10000": "$s0",
    "10001": "$s1",
    "10010": "$s2",
    "10011": "$s3",
    "10100": "$s4",
    "10101": "$s5",
    "10110": "$s6",
    "10111": "$s7",
    "11000": "$t8",
    "11001": "$t9",
    "11010": "$k0",
    "11011": "$k1",
    "11100": "$gp",
    "11101": "$sp",
    "11110": "$fp",
    "11111": "$ra",
    "001000": "addi",
    "100000": "add",
    "100011": "lw",
    "101011": "sw",
    "100010": "sub",
    "011000": "mult",
    "011001": "multu",
    "010000": "mfhi",
    "010010": "mflo",
    "011010": "div",
    "001111": "lui",
    "001101": "ori",
    "000100": "beq",
    "000101": "bne",
    "000010": "j",
    "000011": "jal",
    "001000": "jr",
    "101010": "slt",
    "001100": "addiu",
    "100001": "addu",
    "001100": "andi",
    "100100": "lbu",
    "100101": "lhu",
    "110000": "ll",
    "001010": "slti",
    "001011": "sltiu",
    "101011": "sltu",
    "000000": "sll",
    "000010": "srl",
    "101000": "sb",
    "111000": "sc"}



def traduceMips (lista,tipos,registros, hexatobin, MipsRHexa):
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
    modelo1 =[opcode, rs, rt, rd, shamt, funct]
    modelo2 =[opcode, rs, rt, immediate]
    modelo3 =[opcode, address]
    modelo = []

    while flag == False:
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
            modelo = modelo1
            rd = registros[lista[1]]
            rs = registros[lista[2]]
            rt = registros[lista[3]]
            funct = MipsRHexa[lista[0]]

            if lista[0] == "sll":
                shamt = hexatobin[lista[4]]
            
            elif lista[0] == "srl":
                shamt = hexatobin[lista[4]]
            else:
                shamt = "00000"
            

        elif tipo == "I":
            modelo = modelo2
            rs = registros[lista[1]]
            rt = registros[lista[2]]
            immediate = "00000000000" + hexatobin[lista[3]]

        elif tipo == "J":
            modelo = modelo3
        
def swTrasnslater (lista,tipos,registros, hexatobin, MipsRHexa):
        if lista[0]== swCadena:
            opcode = registros[lista[0]] 
            rt = registros[lista[1]]
            immediate=hexatobin[lista[2][1]]
            temp=lista[2][2]+lista[2][3]+lista[2][4]
            rs = registros[temp]

def lwTrasnslater (lista,tipos,registros, hexatobin, MipsRHexa):
        if lista[0]== lwCadena:
            opcode = registros[lista[0]] 
            rt = registros[lista[1]]
            immediate=hexatobin[lista[2][1]]
            temp=lista[2][2]+lista[2][3]+lista[2][4]
            rs = registros[temp]


