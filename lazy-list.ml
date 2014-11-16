module type LAZYLIST = 
sig
  exception TODO

  type 'a susp = Susp of (unit -> 'a)
  val delay : (unit -> 'a) -> 'a susp 
  val force : 'a susp -> 'a 

  type 'a lazy_list = { hd : 'a; tl : 'a fin_list susp; }
  and 'a fin_list = Empty | NonEmpty of 'a lazy_list

  val take : int -> 'a lazy_list -> 'a list  

  val map : ('a -> 'b) -> 'a lazy_list -> 'b lazy_list 

  val append : 'a lazy_list -> 'a lazy_list -> 'a lazy_list (*change signature to be consistant with the assignment document*)
  val natsFrom : int -> int lazy_list 

  val interleave : int -> int list -> int list lazy_list 
  val flatten : 'a lazy_list lazy_list -> 'a lazy_list 

  val permute : int list -> int list lazy_list 
end;; 

module LazyList : LAZYLIST = 
struct

  exception TODO
(* ---------------------------------------------------- *)
(* Suspended computation : we can suspend computation
   by wrapping it in a closure. *)
type 'a susp = Susp of (unit -> 'a)

(* delay: *)
let delay f = Susp(f)

(* force: *)
let force (Susp f) = f ()

(* ---------------------------------------------------- *)
(* We define next a lazy list; this list is possibly
   finite; this is accomplished by a mutual recursive
   datatype.

   'a lazy_list defines a lazy list; we can observe the 
   head and its tail. For the tail we have two options:
   we have reached the end of the list indicated by the 
   constructor Empty or we have not reached the end 
   indicated by the constructor NonEmpty and we expose
   another lazy list of which we can observe the head and the tail.  

*)
type 'a lazy_list = {hd: 'a  ; tl : ('a fin_list) susp} 
and 'a fin_list = Empty | NonEmpty of 'a lazy_list


(* ---------------------------------------------------- *)
(* creating some finite lazy list *)
(*
val natsFrom : int -> int lazy_list =
val natsFrom' : int -> int fin_list =
*)
let rec natsFrom n = 
  { hd = n ; 
    tl = Susp (fun () -> natsFrom' (n-1)) } 

and natsFrom' n = if n < 0 then Empty
  else NonEmpty (natsFrom n)

(* Alternative ...*)
(* val lazy_nats_from : int -> int fin_list *)
let rec lazy_nats_from n = match n with 
  | 0 -> Empty
  | n -> NonEmpty {hd = n ; tl = Susp (fun () -> lazy_nats_from (n-1)) }

(* ---------------------------------------------------- *)
(* We can now rewrite our previous functions on infinite 
   streams for lazy-lists
*)

(* 
   val take : int -> 'a lazy_list -> 'a list 
   val take' : int -> 'a fin_list -> 'a list 
*)
let rec take n s = match n with 
  | 0 -> []
  | n -> s.hd :: take' (n-1) (force s.tl)

and take' n s = match s with 
  | Empty -> [] 
  | NonEmpty s -> take n s

(* ---------------------------------------------------- *)
(* Q4. 1 :

   Hint: It is easiest to solve this problem by implementing
   two mutual recursive functions, one that manipulates lazy lists and
   one that manipulates finite lists. See take for an example.

    val map : ('a -> 'b) -> 'a lazy_list -> 'b lazy_list 
    val map' : ('a -> 'b) -> 'a fin_list -> 'b fin_list 
*)

let rec map f s =
   {
    hd = f(s.hd);
    tl = Susp (fun () -> map_finite_list f (force s.tl))
  }
and map_finite_list f s = match s with
    |Empty -> Empty
    |NonEmpty s -> NonEmpty (map f s)
 

(* ---------------------------------------------------- *)
(* Q4. 2 *)
(*
   Hint: It is easiest to solve this problem by implementing
   two mutual recursive functions, one that manipulates lazy lists and
   one that manipulates finite lists. See take and map for an example.

 val append : 'a lazy_list -> 'a lazy_list -> 'a lazy_list 
 val append' : 'a fin_list -> 'a fin_list -> 'a fin_list 
*)

(*let rec append s1 s2 = 
  {
    hd = s1.hd;
    tl = Susp (fun () -> append_finite_list (force s1.tl) (NonEmpty s2))
  }
  and append_finite_list s1 s2 = match s1, s2 with
    |s1, Empty -> s1
    |Empty, s2 -> s2
    |NonEmpty s1, NonEmpty s2 -> NonEmpty (append s1 s2)*)

let rec append s1 s2 = 
  {
    hd = s1.hd;
    tl = Susp (fun () -> append_finite_list (force s1.tl) (NonEmpty s2))
  }
  and append_finite_list s1 s2 = match s1 with
    |Empty -> s2
    |NonEmpty s -> match s2 with
      |Empty -> s1
      |NonEmpty s'-> NonEmpty (append s s')
  

(* ---------------------------------------------------- *)
(* Q4. 3 *)
(* val interleave : int -> int list -> int list lazy_list *)
let rec interleave (x:int) (l:int list) = match l with
  |[] -> 
    {
      hd = [x];
      tl = Susp (fun () -> Empty)
    }
  |h::t -> 
    {
      hd = x::l;
      tl = Susp (fun () -> NonEmpty (map (fun i -> h::i) (interleave x t)))
    }
(* ---------------------------------------------------- *)
(* Q4. 4 *)
(* val flatten : 'a lazy_list lazy_list -> 'a lazy_list
*)

let rec flatten s = match (force s.tl) with
  |Empty -> s.hd
  |NonEmpty s' -> append s.hd (flatten s')


(* ---------------------------------------------------- *)
(* Permute *)
(* Q4. 5 *)
let lazy_empty = Susp (fun () -> Empty )

let rec permute l = match l with
  |[] -> 
    {
      hd = l;
      tl = lazy_empty
    }
  |hd::tl -> flatten(map (interleave hd) (permute tl))


end
