

Fixed_Cost = 30000
Content_Cost = 70000

member_ff = 15
convert_rate = 0.1
ad_revenue_each_person = 1

num = float(input('please input your estimate number of subscribers:'))

a=0
b=num
c=(a+b)/2


if b < 50000:
    Total_Cost = Fixed_Cost + Content_Cost
else:
    Total_Cost = Fixed_Cost + Content_Cost + 0.1 * (b - 50000)

Revenue = (1*b) + (0.1*15*b)

def profit(s):
    if s < 50000:
        return 2.5 * s - Fixed_Cost - Content_Cost
    else:
        return 2.4 * s - Fixed_Cost - Content_Cost + 0.1*50000


iteration_times = 100
##key step: using for-loop rather than while-loop, idk why

for i in range(0,int(iteration_times)):
    c = (a+b) / 2
    if profit(b) < 0:
        break
    else:
        if profit(a)*profit(c) < 0:
            b = c
        elif profit(a)*profit(c) > 0:
            a = c
if profit(b) >= 0:
    print("\n\nThe break-even point of number of subscribers is {0}, i.e. at the net-profit is {1} at that time\n\n".format(int(c),profit(c)))
else:
    print("\n\nBloody loss money {0} dollar\n\n".format(-profit(b)))

    


    



    
