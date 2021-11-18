clear
close all
clc

%% Lectura de imagen
im_rgb = imread("RGB004.jpg");
% figure('Name','Imagen de entrada','NumberTitle','off');
% imshow(im_rgb)

im_thermal = imread("T007.jpg");
figure('Name','Imagen de entrada','NumberTitle','off');
imshow(im_thermal)

%% Imagen en escala de grises

im_gris_thermal = rgb2gray(im_thermal);

im_gris_rgb = rgb2gray(im_rgb);

im_gris_rgb_resized = imresize(im_gris_rgb,[120 160]);
figure('Name','Imagen redimensionada','NumberTitle','off');
imshow(im_gris_rgb_resized);



%% Creación de filtro threshold
r = 0:255;
m = 240;
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