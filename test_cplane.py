###
# Name: Sook Mun Wong, Chelsea Parlett-Pelleriti
# Student ID: 2303539
# Email: sowong@chapman.edu
# Course: CS510 Fall 2017
# Assignment: CW-05
###

import cplane

def test_cplane():
    a = ListComplexPlane(xmin = 10, xmax = 15, xlen =  5,ymin =2, ymax = 8, ylen = 5)
    assert a == [[(10+2j), (10+5j), (10+8j)], [(12.5+2j), (12.5+5j), (12.5+8j)], [(15+2j), (15+5j), (15+8j)]]
    
    ff = lambda x: x**2
    a.apply(ff)
    assert a == [[(96+40j), (75+100j), (36+160j)], [(152.25+50j), (131.25+125j), (92.25+200j)], [(221+60j), (200+150j), (161+240j)]]
    
    a.zoom(newxmin = 5, newxmax = 10, newxlen =  3,newymin =5, newymax = 10, newylen = 3)
    assert a== [[50j, (-31.25+75j), (-75+100j)], [(31.25+75j), 112.5j, (-43.75+150j)], [(75+100j), (43.75+150j), 200j]]
    
    a.refresh()
    assert a== [[(5+5j), (5+7.5j), (5+10j)], [(7.5+5j), (7.5+7.5j), (7.5+10j)], [(10+5j), (10+7.5j), (10+10j)]]
    
    