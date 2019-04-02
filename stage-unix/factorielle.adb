-- Fichier d'exemple en Ada.
--
-- Pour compiler ce fichier, faites :
--   gnatmake factorielle.adb
-- ce qui creera un fichier factorielle, que l'on peut
-- executer avec :
--   ./factorielle
--
-- Ce fichier calcule une factorielle de plusieurs manieres.

with Ada.Text_IO, Ada.Integer_Text_IO;
use  Ada.Text_IO, Ada.Integer_Text_IO;

procedure Factorielle is
   -- version recursive inefficace.
   function F_Rec(N: Natural) return Positive is
   begin
      if N <= 1 then
         return 1;
      else
         return F_Rec(N-1) * N;
      end if;
   end F_Rec;

   -- version recursive terminale
   function F_Term(N: Natural; Acc: Positive) return Positive is
   begin
      if N <= 1 then
         return Acc;
      else
         return F_Term(N-1, Acc * N);
      end if;
   end F_Term;

   -- version iterative
   function F_Imperative(N: Natural) return Positive is
      Res : Positive := 1;
   begin
      for I in 2..N loop
         Res := Res * I;
      end loop;
      return Res;
   end F_Imperative;

   Val : Integer;
begin
   Put_Line("Entrez une valeur :");
   Get(Val);
   Put_Line("La factorielle (calculee recursivement) de" &
              Integer'Image(Val) &
              " est :" &
              Integer'Image(F_Rec(Val)) &
              ".");
   Put_Line("La factorielle (calculee avec une fonction recursive terminale) de" &
              Integer'Image(Val) &
              " est :" &
              Integer'Image(F_Term(Val, 1)) &
              ".");
   Put_Line("La factorielle (calculee avec une boucle) de" &
              Integer'Image(Val) &
              " est :" &
              Integer'Image(F_Imperative(Val)) &
              ".");
end Factorielle;
