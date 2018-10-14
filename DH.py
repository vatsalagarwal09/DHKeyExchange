

# As y doubles in magnitude, each additional bit requires another recursive round to remove it. This makes this function = O(n)
def mod_exp(x, y, N):
    # This function implements an algorithm to solve modular exponentiation problems more efficiently than simply evaluating the entire exponetial statement and then modding it, since this method does not scale well. Instead, we will first check if power == 0. If yes, we return 1.
    if y == 0:
        return 1

    # Otherwise, we recursively call this function but pass in half the value of power (integer division aka floor division). This results in a stack of recursive calls until power reaches zero, at which point the function returns 1 and begins to unwind.
    z = mod_exp(x, y // 2, N)

    # Each function call then takes the value returned from the recursive layer under it and puts it into a new variable Z. The function then checks if power in the current context is even.
    if y % 2 == 0:
        # If it is, the function returns Z^2 % mod.
        return z ** 2 % N
    else:
        # If it isn't, then the function returns number * z^2 % mod.
        return (x * z ** 2) % N

    # The final layer will return the completed answer, having kept the size of the numbers involved down to a reasonable level by modding the results of every step, rather than just at the end.


def truncate_int(integer, digits_to_truncate):
    if (digits_to_truncate > 0):
        truncatingDivisor = 10**truncateLength
        integer = integer//truncatingDivisor
    return integer

#used for debugging purposes & maybe later expansion of this code.
def find_int_truncate_length(smallerSizeInt, largerSizeInt):
    return (len(str(largerSizeInt))) - (len(str(smallerSizeInt)))


# generated from bash with command: openssl prime -generate -bits 504 -safe
#p = 50124742423032139575529932728461966889289625472757235332001917562677753334238590371036458592425769162001675049822480235742252378403035818995349570833399
p = int(input("Prime for modulus:\n"))
# generated from bash with command: od -vAn -N66 -tu8 < /dev/urandom. I had to remove the spaces and contatenate all the numbers together because my machine is not capable of producing unsigned integers with bit sizes larger than 64.
#a = 2006343205164040606710479947100188344249830292517864959464526692922023880357114526228344084699632631871157918566050179411821258103877659638308392144717642812
a = int(input("Secret exponent:\n"))

# given in specs
#g = 5
g = int(input("Generator:\n"))

gPOWaMODp = mod_exp(g, a, p)

print("Generating value for key exchange...")
# print("p = ", p)
# print("a = ", a)
# print("g = ", g)

print("g^a (mod p) = ", gPOWaMODp)

# taken from server
#b = 1998286638065473057944506344030256054916203227381748916180906390214373930105605405985818224246280726328877245115163209963634633681313092395058312190549

# taken from server response
#gPOWbMODp = 44496357379705649538211157451040520972135112119334221960821471214592045319104075380895047686366873599805775697591876748960587653748773508883955160499375
gPOWbMODp = int(input("Shared key from server:\n"))
# computed by server
#correctSharedValue  = 171241840000005032593602255680220012275917712065520042065564619694982037055158164346468462400848623996

#computedSharedValueAB = 17124184000000503259360225568022001227591771206552004206556461969498203705515816434646846240084862399633135668933346970318363774901190528482316469654252

#computedCorrectly = gPOWbMODp == mod_exp(g, b, p)

#print("g^b computed correctly? ", computedCorrectly)

#computedSharedValueAB = mod_exp(gPOWaMODp, b, p)

#computedSharedValueLength = len(str(computedSharedValueAB))

#truncateLength = find_int_truncate_length(correctSharedValue, computedSharedValueAB)

#computedSharedValueAB = truncate_int(computedSharedValueAB, truncateLength)

#computedCorrectly = correctSharedValue == computedSharedValueAB

#print("(g^b)^a (mod p) computed correctly? ", computedCorrectly)

#if computedCorrectly:
#    print("Shared value is: ", computedSharedValueAB)
#else:
#    print("Incorrect shared value is: ", computedSharedValueAB)

computedSharedValueBA = mod_exp(gPOWbMODp, a, p)

#truncateLength = 50  # find_int_truncate_length(correctSharedValue, computedSharedValueBA)
truncateLength = int(input("Truncate of shared value length:\n"))

computedSharedValueBA = truncate_int(computedSharedValueBA, truncateLength)

print("Shared value is: ", computedSharedValueBA)

#computedCorrectly = correctSharedValue == computedSharedValueBA

#print("(g^a)^b (mod p) computed correctly? ", computedCorrectly)

#if computedCorrectly:
#    print("Shared value is: ", computedSharedValueBA)
#else:
#    print("Incorrect shared value is: ", computedSharedValueBA)