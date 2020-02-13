from display import *
from draw import *
from matrix import *

s = new_screen()
c = [ 0, 255, 0 ]
matrix = new_matrix()

identity = new_matrix()
ident(identity)
# identity[0][0] = 2
# identity[1][1] = 2
# identity[2][2] = 2
# identity[3][3] = 2

add_edge(matrix, 50, 450, 0, 100, 450, 0);
add_edge(matrix, 50, 450, 0, 50, 400, 0);
add_edge(matrix, 100, 450, 0, 100, 400, 0);
add_edge(matrix, 100, 400, 0, 50, 400, 0);

add_edge(matrix, 200, 450, 0, 250, 450, 0);
add_edge(matrix, 200, 450, 0, 200, 400, 0);
add_edge(matrix, 250, 450, 0, 250, 400, 0);
add_edge(matrix, 250, 400, 0, 200, 400, 0);

add_edge(matrix, 150, 400, 0, 130, 360, 0);
add_edge(matrix, 150, 400, 0, 170, 360, 0);
add_edge(matrix, 130, 360, 0, 170, 360, 0);

add_edge(matrix, 100, 340, 0, 200, 340, 0);
add_edge(matrix, 100, 320, 0, 200, 320, 0);
add_edge(matrix, 100, 340, 0, 100, 320, 0);
add_edge(matrix, 200, 340, 0, 200, 320, 0);

# print_matrix(matrix)

matrix_mult(identity, matrix)

# print_matrix(matrix)
draw_lines( matrix, s, c )

save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
