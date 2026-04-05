front_red=[
    ['R','R','R'],
    ['R','R','R'],
    ['R','R','R'],
]
back_orange=[
    ['O','O','O'],
   ['O','O','O'],
    ['O','O','O'],
]
up_white=[
    
        ['W','W','W'],
        ['W','W','W'],
        ['W','W','W'],
    ]
  
down_yellow=[

    ['Y','Y','Y'],
    ['Y','Y','Y'],
    ['Y','Y','Y'],
] 
left_green=[

    ['G','G','G'],
    ['G','G','G'],
    ['G','G','G'],
]

Right_blue=[
    
        ['B','B','B'],
        ['B','B','B'],
        ['B','B','B'], 
]
cube=[front_red,back_orange,up_white,down_yellow,left_green,Right_blue,]
#print(cube[0])
#print(cube[2][2])
#print(cube[2][2][1])

def rotate_face_clockwise(face):
    new_face=[['0','0','0'],
              ['0','0','0'],
              ['0','0','0']]
    for i in range(3):
        for j in range(3):
            new_face[i][j]=face[2-j][i]
    return new_face

#cube[0]=rotate_face_clockwise(cube[0])
#print(cube[0])
#cube[2][2]  → cube[5][*][0]
#cube[5][*][0] → cube[3][0]
#cube[3][0] → cube[4][*][2]
#cube[4][*][2] → cube[2][2]

def rotate_front_f(cube):
    temp=cube[2][2].copy()
    cube[2][2] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
    cube[4][0][2] = cube[3][0][0]
    cube[4][1][2] = cube[3][0][1]
    cube[4][2][2] = cube[3][0][2]

    cube[3][0] = [cube[5][0][0], cube[5][1][0], cube[5][2][0]]
    cube[5][0][0]=cube[2][2][0],cube[2][2][1],cube[2][2][2]
    cube[5][1][0]=
    cube[5][2][0]

    
    
