-- solution2.hs

module Solution2 where

lampfishMaxDays = 8

countLampfish :: [Int] -> [Int]
countLampfish [] = map (const 0) [0..lampfishMaxDays]
countLampfish list = map (`countOccurance` list) [0..lampfishMaxDays]

countOccurance :: Eq a => a -> [a] -> Int
countOccurance _ [] = 0
countOccurance x xs = length $ filter (== x) xs

iterateDay [a, b, c, d, e, f, g, h, i] = [b, c, d, e, f, g, h+a, i, a]
iterateDays n list = iterate iterateDay list !! n

solution days list = sum $ iterateDays days $ countLampfish list

