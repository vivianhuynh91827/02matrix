from display import *
from draw import *
from matrix import *

s = new_screen()
c = [ 0,0,0 ]
m2 = new_matrix(rows = 0, cols = 0)
m1 = new_matrix()

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("Testing ident. m1 =")
ident(m1)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

print("Testing Matrix mult. m1 =")
m1 = new_matrix(rows = 0, cols = 0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)


matrix = new_matrix()
X = 0
Y = 1

points = [
[72,20], #0
[28,10], #1
[22,14], #2
[24,18], #3
[22,24], #4
[28,22], #5
[32,22], #6
[38,24], #7
[29,26], #8
[24,30], #9
[30,32], #10
[30,37], #11
[38,38], #12
[37,41], #13
[32,44], #14
[34,48], #15
[36,52], #16
[38,92], #17
[44,16], #18
[50,21], #19
[47,29], #20
[47,34], #21
[50,35], #22
[47,41], #23
[44,43], #24
[54,43], #25
[51,44], #26
[44,46], #27
[56,46], #28
[52,48], #29
[42,49], #30
[50,51], #31
[47,54], #32
[42,55], #33
[49,56], #34
[53,56], #35
[57,56], #36
[51,61], #37
[54,66], #38
[58,67], #39
[52,72], #40
[58,72], #41
[50,73], #42
[50,78], #43
[43,80], #44
[54,82], #45
[44,102], #46
[52,106], #47
[56,110], #48
[73,28], #49
[76,30], #50
[74,36], #51
[76,40], #52
[70,44], #53
[64,46], #54
[78,46], #55
[69,48], #56
[61,50], #57
[72,50], #58
[76,52], #59
[70,56], #60
[66,56], #61
[72,57], #62
[71,62], #63
[65,67], #64
[69,66], #65
[65,72], #66
[73,71], #67
[68,80], #68
[73,82], #69
[64,88], #70
[76,91], #71
[72,94], #72
[75,98], #73
[67,102], #74
[64,107], #75
[70,102], #76
[95,10], #77
[85,19], #78
[90,20], #79
[99,18], #80
[91,23], #81
[95,24], #82
[94,28], #83
[96,30], #84
[88,34], #85
[90,38], #86
[80,42], #87
[88,44], #88
[80,48], #89
[87,48], #90
[86,52], #91
[80,55], #92
[71,42] #93
]

for point in points:
    point[X] = point[X] * 8
    point[Y] = point[Y] * 8

add_edge(matrix, points[1][X], points[1][Y], 0, points[2][X], points[2][Y], 0) #1
add_edge(matrix, points[4][X], points[4][Y], 0, points[2][X], points[2][Y], 0) #2

add_edge(matrix, points[1][X], points[1][Y], 0, points[3][X], points[3][Y], 0) #3
add_edge(matrix, points[3][X], points[3][Y], 0, points[4][X], points[4][Y], 0) #4

add_edge(matrix, points[4][X], points[4][Y], 0, points[9][X], points[9][Y], 0) #5
add_edge(matrix, points[3][X], points[3][Y], 0, points[9][X], points[9][Y], 0) #6

add_edge(matrix, points[3][X], points[3][Y], 0, points[5][X], points[5][Y], 0) #7
add_edge(matrix, points[5][X], points[5][Y], 0, points[9][X], points[9][Y], 0) #8

add_edge(matrix, points[5][X], points[5][Y], 0, points[6][X], points[6][Y], 0) #9
add_edge(matrix, points[9][X], points[9][Y], 0, points[8][X], points[8][Y], 0) #10

add_edge(matrix, points[9][X], points[9][Y], 0, points[10][X], points[10][Y], 0) #11
add_edge(matrix, points[8][X], points[8][Y], 0, points[10][X], points[10][Y], 0) #12

add_edge(matrix, points[8][X], points[8][Y], 0, points[7][X], points[7][Y], 0) #13
add_edge(matrix, points[7][X], points[7][Y], 0, points[18][X], points[18][Y], 0) #14

add_edge(matrix, points[6][X], points[6][Y], 0, points[18][X], points[18][Y], 0) #15
add_edge(matrix, points[9][X], points[9][Y], 0, points[11][X], points[11][Y], 0) #16

add_edge(matrix, points[10][X], points[10][Y], 0, points[13][X], points[13][Y], 0) #17
add_edge(matrix, points[10][X], points[10][Y], 0, points[12][X], points[12][Y], 0) #18

add_edge(matrix, points[11][X], points[11][Y], 0, points[13][X], points[13][Y], 0) #19
add_edge(matrix, points[13][X], points[13][Y], 0, points[24][X], points[24][Y], 0) #20

add_edge(matrix, points[12][X], points[12][Y], 0, points[23][X], points[23][Y], 0) #21
add_edge(matrix, points[23][X], points[23][Y], 0, points[26][X], points[26][Y], 0) #22

add_edge(matrix, points[26][X], points[26][Y], 0, points[28][X], points[28][Y], 0) #23
add_edge(matrix, points[21][X], points[21][Y], 0, points[26][X], points[26][Y], 0) #24

add_edge(matrix, points[21][X], points[21][Y], 0, points[25][X], points[25][Y], 0) #25
add_edge(matrix, points[22][X], points[22][Y], 0, points[25][X], points[25][Y], 0) #26

add_edge(matrix, points[21][X], points[21][Y], 0, points[20][X], points[20][Y], 0) #27
add_edge(matrix, points[20][X], points[20][Y], 0, points[22][X], points[22][Y], 0) #28

add_edge(matrix, points[19][X], points[19][Y], 0, points[22][X], points[22][Y], 0) #29
add_edge(matrix, points[20][X], points[20][Y], 0, points[19][X], points[19][Y], 0) #30

add_edge(matrix, points[24][X], points[24][Y], 0, points[29][X], points[29][Y], 0) #31
add_edge(matrix, points[28][X], points[28][Y], 0, points[29][X], points[29][Y], 0) #32

add_edge(matrix, points[12][X], points[12][Y], 0, points[24][X], points[24][Y], 0) #33
add_edge(matrix, points[25][X], points[25][Y], 0, points[28][X], points[28][Y], 0) #34

add_edge(matrix, points[14][X], points[14][Y], 0, points[27][X], points[27][Y], 0) #35
add_edge(matrix, points[14][X], points[14][Y], 0, points[30][X], points[30][Y], 0) #36

add_edge(matrix, points[14][X], points[14][Y], 0, points[15][X], points[15][Y], 0) #37
add_edge(matrix, points[15][X], points[15][Y], 0, points[32][X], points[32][Y], 0) #38

add_edge(matrix, points[15][X], points[15][Y], 0, points[16][X], points[16][Y], 0) #39
add_edge(matrix, points[16][X], points[16][Y], 0, points[32][X], points[32][Y], 0) #40

add_edge(matrix, points[16][X], points[16][Y], 0, points[33][X], points[33][Y], 0) #41
add_edge(matrix, points[33][X], points[33][Y], 0, points[34][X], points[34][Y], 0) #42

add_edge(matrix, points[31][X], points[31][Y], 0, points[34][X], points[34][Y], 0) #43
add_edge(matrix, points[27][X], points[27][Y], 0, points[31][X], points[31][Y], 0) #44

add_edge(matrix, points[30][X], points[30][Y], 0, points[32][X], points[32][Y], 0) #45
add_edge(matrix, points[31][X], points[31][Y], 0, points[29][X], points[29][Y], 0) #46

add_edge(matrix, points[29][X], points[29][Y], 0, points[36][X], points[36][Y], 0) #47
add_edge(matrix, points[34][X], points[34][Y], 0, points[35][X], points[35][Y], 0) #48

add_edge(matrix, points[35][X], points[35][Y], 0, points[36][X], points[36][Y], 0) #49
add_edge(matrix, points[36][X], points[36][Y], 0, points[57][X], points[57][Y], 0) #50

add_edge(matrix, points[28][X], points[28][Y], 0, points[57][X], points[57][Y], 0) #51
add_edge(matrix, points[57][X], points[57][Y], 0, points[54][X], points[54][Y], 0) #52

add_edge(matrix, points[57][X], points[57][Y], 0, points[61][X], points[61][Y], 0) #53
add_edge(matrix, points[34][X], points[34][Y], 0, points[37][X], points[37][Y], 0) #54

add_edge(matrix, points[35][X], points[35][Y], 0, points[39][X], points[39][Y], 0) #55
add_edge(matrix, points[36][X], points[36][Y], 0, points[39][X], points[39][Y], 0) #56

add_edge(matrix, points[37][X], points[37][Y], 0, points[40][X], points[40][Y], 0) #57
add_edge(matrix, points[37][X], points[37][Y], 0, points[38][X], points[38][Y], 0) #58

add_edge(matrix, points[37][X], points[37][Y], 0, points[39][X], points[39][Y], 0) #59
add_edge(matrix, points[38][X], points[38][Y], 0, points[41][X], points[41][Y], 0) #60

add_edge(matrix, points[38][X], points[38][Y], 0, points[45][X], points[45][Y], 0) #61
add_edge(matrix, points[40][X], points[40][Y], 0, points[45][X], points[45][Y], 0) #62

add_edge(matrix, points[40][X], points[40][Y], 0, points[42][X], points[42][Y], 0) #63
add_edge(matrix, points[42][X], points[42][Y], 0, points[43][X], points[43][Y], 0) #64

add_edge(matrix, points[43][X], points[43][Y], 0, points[45][X], points[45][Y], 0) #65
add_edge(matrix, points[43][X], points[43][Y], 0, points[44][X], points[44][Y], 0) #66

add_edge(matrix, points[44][X], points[44][Y], 0, points[45][X], points[45][Y], 0) #67
add_edge(matrix, points[17][X], points[17][Y], 0, points[44][X], points[44][Y], 0) #68

add_edge(matrix, points[17][X], points[17][Y], 0, points[45][X], points[45][Y], 0) #69
add_edge(matrix, points[45][X], points[45][Y], 0, points[46][X], points[46][Y], 0) #70
#
add_edge(matrix, points[45][X], points[45][Y], 0, points[47][X], points[47][Y], 0) #71
add_edge(matrix, points[48][X], points[48][Y], 0, points[70][X], points[70][Y], 0) #72

add_edge(matrix, points[17][X], points[17][Y], 0, points[46][X], points[46][Y], 0) #73
add_edge(matrix, points[46][X], points[46][Y], 0, points[47][X], points[47][Y], 0) #74

add_edge(matrix, points[47][X], points[47][Y], 0, points[48][X], points[48][Y], 0) #75
add_edge(matrix, points[48][X], points[48][Y], 0, points[75][X], points[75][Y], 0) #76

add_edge(matrix, points[45][X], points[45][Y], 0, points[70][X], points[70][Y], 0) #77
add_edge(matrix, points[41][X], points[41][Y], 0, points[70][X], points[70][Y], 0) #78

add_edge(matrix, points[39][X], points[39][Y], 0, points[41][X], points[41][Y], 0) #79
add_edge(matrix, points[39][X], points[39][Y], 0, points[64][X], points[64][Y], 0) #80

add_edge(matrix, points[64][X], points[64][Y], 0, points[66][X], points[66][Y], 0) #81
add_edge(matrix, points[41][X], points[41][Y], 0, points[66][X], points[66][Y], 0) #82

add_edge(matrix, points[41][X], points[41][Y], 0, points[64][X], points[64][Y], 0) #83
add_edge(matrix, points[39][X], points[39][Y], 0, points[66][X], points[66][Y], 0) #84

add_edge(matrix, points[74][X], points[74][Y], 0, points[75][X], points[75][Y], 0) #85
add_edge(matrix, points[74][X], points[74][Y], 0, points[72][X], points[72][Y], 0) #86

add_edge(matrix, points[75][X], points[75][Y], 0, points[76][X], points[76][Y], 0) #87
add_edge(matrix, points[70][X], points[70][Y], 0, points[74][X], points[74][Y], 0) #88

add_edge(matrix, points[73][X], points[73][Y], 0, points[76][X], points[76][Y], 0) #89
add_edge(matrix, points[71][X], points[71][Y], 0, points[73][X], points[73][Y], 0) #90

add_edge(matrix, points[72][X], points[72][Y], 0, points[76][X], points[76][Y], 0) #91
add_edge(matrix, points[71][X], points[71][Y], 0, points[72][X], points[72][Y], 0) #92

add_edge(matrix, points[70][X], points[70][Y], 0, points[72][X], points[72][Y], 0) #93
add_edge(matrix, points[69][X], points[69][Y], 0, points[72][X], points[72][Y], 0) #94

add_edge(matrix, points[69][X], points[69][Y], 0, points[71][X], points[71][Y], 0) #95
add_edge(matrix, points[70][X], points[70][Y], 0, points[66][X], points[66][Y], 0) #96

add_edge(matrix, points[70][X], points[70][Y], 0, points[68][X], points[68][Y], 0) #97
add_edge(matrix, points[67][X], points[67][Y], 0, points[68][X], points[68][Y], 0) #98

add_edge(matrix, points[67][X], points[67][Y], 0, points[69][X], points[69][Y], 0) #99
add_edge(matrix, points[65][X], points[65][Y], 0, points[68][X], points[68][Y], 0) #100

add_edge(matrix, points[63][X], points[63][Y], 0, points[67][X], points[67][Y], 0) #101
add_edge(matrix, points[65][X], points[65][Y], 0, points[66][X], points[66][Y], 0) #102

add_edge(matrix, points[63][X], points[63][Y], 0, points[64][X], points[64][Y], 0) #103
add_edge(matrix, points[61][X], points[61][Y], 0, points[64][X], points[64][Y], 0) #104

add_edge(matrix, points[64][X], points[64][Y], 0, points[60][X], points[60][Y], 0) #105
add_edge(matrix, points[62][X], points[62][Y], 0, points[63][X], points[63][Y], 0) #106

add_edge(matrix, points[60][X], points[60][Y], 0, points[61][X], points[61][Y], 0) #107
add_edge(matrix, points[60][X], points[60][Y], 0, points[62][X], points[62][Y], 0) #108

add_edge(matrix, points[61][X], points[61][Y], 0, points[56][X], points[56][Y], 0) #109
add_edge(matrix, points[62][X], points[62][Y], 0, points[92][X], points[92][Y], 0) #110

add_edge(matrix, points[91][X], points[91][Y], 0, points[92][X], points[92][Y], 0) #111
add_edge(matrix, points[59][X], points[59][Y], 0, points[91][X], points[91][Y], 0) #112

add_edge(matrix, points[59][X], points[59][Y], 0, points[90][X], points[90][Y], 0) #113
add_edge(matrix, points[90][X], points[90][Y], 0, points[91][X], points[91][Y], 0) #114

add_edge(matrix, points[90][X], points[90][Y], 0, points[88][X], points[88][Y], 0) #115
add_edge(matrix, points[88][X], points[88][Y], 0, points[89][X], points[89][Y], 0) #116

add_edge(matrix, points[59][X], points[59][Y], 0, points[89][X], points[89][Y], 0) #117
add_edge(matrix, points[55][X], points[55][Y], 0, points[88][X], points[88][Y], 0) #118

add_edge(matrix, points[58][X], points[58][Y], 0, points[55][X], points[55][Y], 0) #119
add_edge(matrix, points[62][X], points[62][Y], 0, points[58][X], points[58][Y], 0) #120

add_edge(matrix, points[56][X], points[56][Y], 0, points[58][X], points[58][Y], 0) #121
add_edge(matrix, points[54][X], points[54][Y], 0, points[56][X], points[56][Y], 0) #122

add_edge(matrix, points[28][X], points[28][Y], 0, points[54][X], points[54][Y], 0) #123
add_edge(matrix, points[56][X], points[56][Y], 0, points[87][X], points[87][Y], 0) #124

add_edge(matrix, points[53][X], points[53][Y], 0, points[54][X], points[54][Y], 0) #125
add_edge(matrix, points[53][X], points[53][Y], 0, points[87][X], points[87][Y], 0) #126

add_edge(matrix, points[53][X], points[53][Y], 0, points[93][X], points[93][Y], 0) #127
add_edge(matrix, points[51][X], points[51][Y], 0, points[93][X], points[93][Y], 0) #128

add_edge(matrix, points[93][X], points[93][Y], 0, points[52][X], points[52][Y], 0) #129
add_edge(matrix, points[51][X], points[51][Y], 0, points[54][X], points[54][Y], 0) #130

add_edge(matrix, points[54][X], points[54][Y], 0, points[49][X], points[49][Y], 0) #131
add_edge(matrix, points[49][X], points[49][Y], 0, points[51][X], points[51][Y], 0) #132

add_edge(matrix, points[50][X], points[50][Y], 0, points[51][X], points[51][Y], 0) #133
add_edge(matrix, points[0][X], points[0][Y], 0, points[50][X], points[50][Y], 0) #134

add_edge(matrix, points[0][X], points[0][Y], 0, points[49][X], points[49][Y], 0) #135
add_edge(matrix, points[52][X], points[52][Y], 0, points[85][X], points[85][Y], 0) #136

add_edge(matrix, points[52][X], points[52][Y], 0, points[86][X], points[86][Y], 0) #137
add_edge(matrix, points[86][X], points[86][Y], 0, points[87][X], points[87][Y], 0) #138

add_edge(matrix, points[85][X], points[85][Y], 0, points[86][X], points[86][Y], 0) #139
add_edge(matrix, points[85][X], points[85][Y], 0, points[83][X], points[83][Y], 0) #140

add_edge(matrix, points[83][X], points[83][Y], 0, points[86][X], points[86][Y], 0) #141
add_edge(matrix, points[84][X], points[84][Y], 0, points[86][X], points[86][Y], 0) #142

add_edge(matrix, points[81][X], points[81][Y], 0, points[83][X], points[83][Y], 0) #143
add_edge(matrix, points[78][X], points[78][Y], 0, points[81][X], points[81][Y], 0) #144

add_edge(matrix, points[78][X], points[78][Y], 0, points[79][X], points[79][Y], 0) #145
add_edge(matrix, points[81][X], points[81][Y], 0, points[79][X], points[79][Y], 0) #146

add_edge(matrix, points[79][X], points[79][Y], 0, points[82][X], points[82][Y], 0) #147
add_edge(matrix, points[82][X], points[82][Y], 0, points[84][X], points[84][Y], 0) #148

add_edge(matrix, points[80][X], points[80][Y], 0, points[84][X], points[84][Y], 0) #149
add_edge(matrix, points[83][X], points[83][Y], 0, points[84][X], points[84][Y], 0) #150

add_edge(matrix, points[80][X], points[80][Y], 0, points[82][X], points[82][Y], 0) #151
add_edge(matrix, points[82][X], points[82][Y], 0, points[77][X], points[77][Y], 0) #152

add_edge(matrix, points[77][X], points[77][Y], 0, points[80][X], points[80][Y], 0) #153
add_edge(matrix, points[6][X], points[6][Y], 0, points[8][X], points[8][Y], 0) #154

add_edge(matrix, points[63][X], points[63][Y], 0, points[65][X], points[65][Y], 0) #155
add_edge(matrix, points[59][X], points[59][Y], 0, points[62][X], points[62][Y], 0) #156

add_edge(matrix, points[32][X], points[32][Y], 0, points[34][X], points[34][Y], 0) #157

# print_matrix(matrix)
draw_lines( matrix, s, c )

save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
