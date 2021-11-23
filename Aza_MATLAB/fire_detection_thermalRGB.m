clear
close all
clc

%% Imagen térmica

im_thermal_leida = imread("Database/T007.jpg");
% figure('Name','Imagen de entrada','NumberTitle','off');
% imshow(im_thermal_leida)
im_thermal = imresize(im_thermal_leida,[240 320]);
figure('Name','Imagen térmica','NumberTitle','off');
imshow(im_thermal);

im_gris_thermal = rgb2gray(im_thermal);
figure('Name','Imagen térmica','NumberTitle','off');
imshow(im_gris_thermal);

r = 0:255;
m = 225;
s = zeros(1, 256);

% Threshold
for k = 1:256
    if r(k) >= m
        s(k) = 255;
    end
end

[fil, col, channel] = size(im_gris_thermal);
im_filtrada = uint8(zeros(fil, col));

for i = 1:fil
    for j = 1:col
        r = im_gris_thermal(i,j);
        k = r + 1;
        im_filtrada(i,j) = s(k);
    end
end

figure('Name','Imagen Threshold Thermal','NumberTitle','off');
imshow(im_filtrada)

%% Imagen RGB
im_RGB_leida = imread("Database/RGB004.jpg");
% figure('Name','Imagen de entrada','NumberTitle','off');
% imshow(im_leida)

im_rgb = imresize(im_RGB_leida,[240 320]);
figure('Name','Imagen RGB','NumberTitle','off');
imshow(im_rgb);

imagen_regla_1 = Regla_1(im_rgb);
imagen_regla_2 = Regla_2(im_rgb);
imagen_regla_3 = Regla_3(im_rgb);
imagen_regla_4 = Regla_4(im_rgb);
imagen_regla_5 = Regla_5(im_rgb);
imagen_regla_6 = Regla_6(im_rgb);
imagen_regla_7 = Regla_7(im_rgb);

% Verde es fuego
[fil, col, channel] = size(im_rgb);
fire_pixels = double(zeros(fil, col));
filtered_image = im_rgb;


for x = 1:fil
    for y = 1:col
        if imagen_regla_1(x, y) == 1 && imagen_regla_2(x, y) == 1 && imagen_regla_3(x, y) == 1 && imagen_regla_4(x, y) == 1 && imagen_regla_5(x, y) == 1 && imagen_regla_6(x, y) == 1 && imagen_regla_7(x, y) == 1 
            fire_pixels(x, y) = 255;
            filtered_image(x, y, 1) = 0;
            filtered_image(x, y, 2) = 255;
            filtered_image(x, y, 3) = 0;
        end
    end
end

fire_pixels = uint8(fire_pixels);
figure('Name','Pixeles de fuego','NumberTitle','off');
imshow(fire_pixels)

filtered_image = uint8(filtered_image);
% figure('Name','Imagen filtrada','NumberTitle','off');
% imshow(filtered_image)
