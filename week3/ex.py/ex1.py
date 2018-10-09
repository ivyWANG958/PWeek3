student_list =[
18421111,
18421112,
18421113,
18421114,
18421115,
18421116,
18421117,
18421118,
18421119,
18421120,
18421121,
18421122,
18421123,
18421124,
18421125,
18421126,
18421127,
18421128,
18421129,
18421130,
18421131,
18421132,
18421133,
18421134,
18421135,
18421136,
18421137,
18421138,
18421139,
18421140,
18421141,
18421142,
18421143,
18421144,
18421145,
18421146,
18421147,
18421148,
18421149,
18421150,
18421151,
18421152,
18421153,
18421154,
18421155,
18421156,
18421157,
18421158,
18421159,
18421160
    ]
case_list =[
    'case1 - build a calculator to evaluate your business model',
    'case2 - build a automatic earthquake robot to broadcast the new earthquake',
    'case3 - evaluate social media performance of a luxury brand',
    'case4 - study movie blockbuster \'Dying to Survive\'',
    'case5 - invest your money like the Internet giant, Tencent',
    'case6 - where are the 200,000 inferior vaccines flowing?',
    'case7 - study classics, Who control the discourse power in \'Dream of the Red Chamber\'',
    'case8 - research about Didi-driver crimes in China',
    'case9 - \'Me too\' analysis',
    'case10 - what is hip-hop in china?'
    ]

import random

for i in student_list: 
    for w in case_list:
        i = random.sample(student_list, len(student_list))
        dict = {w :i}
        print dict
        
    break



