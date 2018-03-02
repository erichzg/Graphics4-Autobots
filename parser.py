from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    ident(transform)
    file = open(fname, 'r')
    script_lines = file.readlines()
    for line_num in range(len(script_lines)):
        
        print(script_lines[line_num])
        
        if "line" in script_lines[line_num]:
            print("processing line")
            lp = script_lines[line_num + 1].split()
            print("Points: " + str(lp))
            add_edge(points, float(lp[0]), float(lp[1]), float(lp[2]), float(lp[3]), float(lp[4]), float(lp[5]))
            
        elif "ident" in script_lines[line_num]:
            print("resetting transform")
            ident(transform)
            
        elif "scale" in script_lines[line_num]:
            print("scaling")
            lp = script_lines[line_num + 1].split()
            scale_mat = make_scale(float(lp[0]), float(lp[1]), float(lp[2]))
            matrix_mult(scale_mat, transform)
            
        elif "move" in script_lines[line_num]:
            print("moving")
            lp = script_lines[line_num + 1].split()
            move_mat = make_translate(float(lp[0]), float(lp[1]), float(lp[2]))
            print_matrix(move_mat)
            matrix_mult(move_mat, transform)
            
        elif "rotate" in script_lines[line_num]:
            print("rotating")
            lp = script_lines[line_num + 1].split()
            if lp[0] == 'x':
                rot_mat = make_rotX(float(lp[1]))
            elif lp[0] == 'y':
                rot_mat = make_rotY(float(lp[1]))
            elif lp[0] == 'z':
                rot_mat = make_rotZ(float(lp[1]))
            matrix_mult(rot_mat, transform)
            
        elif "apply" in script_lines[line_num]:
            matrix_mult(transform, points)
            
        elif "display" in script_lines[line_num]:
            print("Edge matrix: " + str(points))
            screen = new_screen()
            draw_lines( points, screen, color )
            display(screen)
            
        elif "save" in script_lines[line_num]:
            lp = script_lines[line_num + 1]
            draw_lines( points, screen, color )
            save_extension(screen, lp)
