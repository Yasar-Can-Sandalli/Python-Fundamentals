# import matematikModule

# matematikModule.carp(2,3)
# matematikModule.topla(2,3)

# import matematikModule as matModule

# matModule.topla(4,6)

# print(matModule.customer["firstName"])

from matematikModule import carp
from matematikModule import topla
from matematikModule import customer

topla(2,9)
carp(7,4)

print(customer["firstName"])