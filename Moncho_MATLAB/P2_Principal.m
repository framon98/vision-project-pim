close all 
clear all

% Imagen Original 
im_RGB = imread("fire_forest.jpg");
figure('Name','Imagen Original');
imshow(im_RGB)

%Figuras de las reglas individuales
figure('Name','Imagen Regla 1');
Regla_1 = R1(im_RGB);
figure('Name','Imagen Regla 2');
Regla_2 = R2(im_RGB);
figure('Name','Imagen Regla 3');
Regla_3 = R3(im_RGB);
figure('Name','Imagen Regla 4');
Regla_4 = R4(im_RGB);
figure('Name','Imagen Regla 5');
Regla_5 = R5(im_RGB);
figure('Name','Imagen Regla 6');
Regla_6 = R6(im_RGB);
figure('Name','Imagen Regla 7');
Regla_7 = R7(im_RGB);


% Parte 2 y 3: Mostrar la imagen con los 7 filtros en blanco y negro y en verde el fuego
[fil, col, channel] = size(im_RGB);
im_7_filtros = double(zeros(fil, col));

for x = 1:fil
    for y = 1:col
        if Regla_1(x, y) == 1 && Regla_2(x, y) == 1 && Regla_3(x, y) == 1 && Regla_4(x, y) == 1 && Regla_5(x, y) == 1 && Regla_6(x, y) == 1 && Regla_7(x, y) == 1 
            im_RGB(x, y, 1) = 0; 
            im_RGB(x, y, 2) = 255;
            im_RGB(x, y, 3) = 0; 
            im_7_filtros(x,y) = 1;
        end
    end
end
figure('Name','Imagen 7 Filtros (Parte 2)');
imshow(im_7_filtros)


figure('Name','Imagen Final(Parte 3)');
imshow(im_RGB)

