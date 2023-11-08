Program main;

Const Max =   100;

Type IntList =   array [0..Max] Of Integer;


function BinarySeach(value: Integer; list: IntList): Integer;
var inf, medium, sup: Integer;
begin
    sup := Max;
    inf := 1;
    medium := (inf + sup) div 2;
    while (inf <= sup) and (list[medium] <> value) do
    begin
        if list[medium] > value then
            sup := medium -1
        else 
            inf := medium +1;
        
        medium := (inf + sup) div 2;
    end;

    if inf > sup then
        medium := -1;
    
    BinarySeach := medium;
end;



Var value, index, return:   Integer;
    list :   IntList;

begin
    for index := 0 to Max do
    begin
        list[index] := index * index;
        WriteLn('[',index,'] => ', list[index] );
          
    end;

    value:= 64;
    return := BinarySeach(value, list);

    WriteLn(value, ' => [', return, ']');



end.