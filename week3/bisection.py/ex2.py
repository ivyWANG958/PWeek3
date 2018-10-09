
Fixed_Cost = 30000
Content_Cost = 70000

member_ff = 15
convert_rate = 0.1
ad_revenue_each_person = 1


def samesign(a,b):
    return a * b > 0 

def bisect(func, low, high):
    assert not samesign(func(low), func(high))

    for x in range(100):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint 
    return midpoint
    

num = float(input('please input your estimate number of subscribers:')) 

if num < 50000:
    Total_Cost = Fixed_Cost + Content_Cost
else:
    Total_Cost = Fixed_Cost + Content_Cost + 0.1 * (num - 50000)

def f(num):    #f(x) = Net_Income
    return (1 * num) + (0.1 * 15 * num) - Total_Cost #Revenue = (1*i) + (0.1*15*i)

x = bisect(f, 0, 50000)
   

if f(num) >= 0:
    print("\n\nThe break-even point of number of subscribers is {0}, i.e. at the net-profit is {1} at that time\n\n".format(int(x),f(num)))
else:
    print("\n\nBloody loss money {0} dollar\n\n".format(-f(num)))


#Q: what's the bisection value here?