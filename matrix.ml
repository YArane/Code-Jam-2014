let multiply x y =
  let xRow = Array.length x
  and yRow = Array.length y in
  let yCol = if yRow = 0 then 0 else Array.length y.(0) in
  let z = Array.make_matrix xRow yCol 0 in
  for i = 0 to xRow-1 do
    for j = 0 to yCol-1 do
      for k = 0 to yRow-1 do
        z.(i).(j) <- z.(i).(j) + x.(i).(k) * y.(k).(j)
      done
    done
  done;
  z

changes!!!

let multiply_stream x y =
  let xRow = 48000
  and yRow = 48000 in
  let yCol = 36450 in
  let z = Array.make_matrix xRow yCol 0 in
  for i = 0 to xRow-1 do
    for j = 0 to yCol-1 do
      for k = 0 to yRow-1 do
        z.(i).(j) <- z.(i).(j) + Stream.next (Stream.next x) * Stream.next (Stream.next y)
      done
    done
  done;                               yCol                 a     b         
  z                                 [      ]   [      ]  [1 2] [1 0] = [1  ]
                               row  [   a  ] * [   b  ]  [3 4] [0 1]   [    ]
                                    [      ]   [      ]      
  for(int i = 0;i < m;i++){  //for all of the rows in a 
      for(int j = 0;j < p;j++){ //for all the col in b
         for(int k = 0;k < n;k++){ // for all the rows in b
            ans[i][j] += a[i][k] * b[k][j];
         }
      }
   }
 



let rec create_list n acc = match n with
  |0 -> acc
  |_ -> create_list (n-1) (n::acc)
  
let rec create_matrix n row acc = match n with
  |0 -> acc
  |_ -> create_matrix (n-1) row (row::acc)

let row = Stream.of_list (create_list 48000 [])


let matrix = Stream.of_list (create_matrix 36450 row [])

let x = Array.of_list [(Array.of_list (create_list 1000000 []));(Array.of_list (create_list 1000000 []));(Array.of_list (create_list 1000000 []))]
in
multiply x x