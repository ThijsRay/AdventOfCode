-- solution1.hs

module Solution1 where

nextDay :: Integer -> [Integer]
nextDay 0 = [6, 8]
nextDay x = [x-1]

iterateSchool :: [Integer] -> [Integer]
iterateSchool [] = []
iterateSchool (x : xs) = concat ([nextDay x] ++ map nextDay xs)

iterateDays :: [Integer] -> Integer -> [Integer]
iterateDays state 0 = state
iterateDays state days = iterateDays (iterateSchool state) (days-1)

solution state days = length $ iterateDays state days
