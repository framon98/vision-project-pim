clear
close all
clc

%% Lectura de imagen
im_rgb = imread("Database/fire_forest.jpg");
figure('Name','Imagen de entrada','NumberTitle','off');
imshow(im_rgb)

%% Reglas
imagen_regla_1 = Regla_1(im_rgb);
imagen_regla_2 = Regla_2(im_rgb);
imagen_regla_3 = Regla_3(im_rgb);
imagen_regla_4 = Regla_4(im_rgb);
imagen_regla_5 = Regla_5(im_rgb);
imagen_regla_6 = Regla_6(im_rgb);
imagen_regla_7 = Regla_7(im_rgb);

%% Verde es fuego
[fil, col, channel] = size(im_rgb);
fire_pixels = double(zeros(fil, col));
filtered_image = im_rgb;


for x = 1:fil
    for y = 1:col
        if imagen_regla_1(x, y) == 1 && imagen_regla_2(x, y) == 1 && imagen_regla_3(x, y) == 1 && imagen_regla_4(x, y) == 1 && imagen_regla_5(x, y) == 1 && imagen_regla_6(x, y) == 1 && imagen_regla_7(x, y) == 1 
            fire_pixels(x, y) = 255;
            filtered_image(x, y, 1) = 127;
            filtered_image(x, y, 2) = 0;
            filtered_image(x, y, 3) = 255;
        end
    end
end

fire_pixels = uint8(fire_pixels);
figure('Name','Pixeles de fuego','NumberTitle','off');
imshow(fire_pixels)

filtered_image = uint8(filtered_image);
figure('Name','Imagen filtrada','NumberTitle','off');
imshow(filtered_image)