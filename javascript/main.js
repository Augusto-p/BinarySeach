function BinarySeach(Dato, ListaOrdenada) {
    let Flag = true;
    let Respuesta = -1;
    let B = ListaOrdenada.length;
    let A = 0;

    while (Flag){
        if (ListaOrdenada[B - Math.floor((B-A)/ 2)] > Dato) {
            B = B - Math.floor((B-A) / 2);
        }else{
            A = B - Math.floor((B-A) / 2);
        }

        if (ListaOrdenada[A + Math.floor((B-A) / 2)]< Dato) {
            A = A + Math.floor((B-A) / 2);
        } else {
            B = A + Math.floor((B-A) / 2);
        }
        
        if (ListaOrdenada[B] == Dato) {
            Flag = false;
            Respuesta = B;
        }
        

    }
    return Respuesta;
    
}

let Numeros = [];

for (let index = 1; index <= 100; index++) {
    Numeros.push(index)
    
}
