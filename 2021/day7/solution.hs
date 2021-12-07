-- solution.hs

module Solution where

fuelCost position destination = abs $ position - destination
fuelCost2 position destination = let distance = abs $ position - destination
                                 in distance*(distance+1) `div` 2

movingCost crabs cost position = sum $ map (`cost` position) crabs

fullRange list = [minimum list..maximum list]

solution' crabs cost = minimum $ map (movingCost crabs cost) (fullRange crabs)

solution1 crabs = solution' crabs fuelCost
solution2 crabs = solution' crabs fuelCost2
