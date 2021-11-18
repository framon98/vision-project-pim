clear
close all
clc

%% Lectura de imagen
im_rgb = imread("RGB004.jpg");
% figure('Name','Imagen de entrada','NumberTitle','off');
% imshow(im_rgb)

%% Imagen en escala de grises
im_gris = rgb2gray(im_rgb);
% figure('Name','Imagen Gris','NumberTitle','off');
% imshow(im_gris);

im_resized = imresize(im_gris,[120 160]);
figure('Name','Imagen redimensionada','NumberTitle','off');
imshow(im_resized);
