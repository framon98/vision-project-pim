function im_filtro = R6(im_rule_6)

[fil, col, ch] = size(im_rule_6);
im_YCbCr = rgb2ycbcr(im_rule_6);
im_filtro = double(zeros(fil, col));
th = 70;

% Inicializacion del vector de la imagen filtrada
im_Y = double(zeros(fil, col));
im_Cb = double(zeros(fil, col));
im_Cr = double(zeros(fil, col));

im_Y = double(im_YCbCr(:, :, 1));
im_Cb = double(im_YCbCr(:, :, 2));
im_Cr = double(im_YCbCr(:, :, 3));

for x = 1:fil
    for y = 1:col
        if abs(im_Cb(x, y) - im_Cr(x, y)) >= th
            im_filtro(x, y) = 1;
        else
            im_filtro(x, y) = 0;
        end
    end
end

imshow(im_filtro)
end 