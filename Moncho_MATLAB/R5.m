function im_filtro = R5(im_rule_5)

[fil, col, ch] = size(im_rule_5);
im_YCbCr = rgb2ycbcr(im_rule_5);
im_filtro = double(zeros(fil, col));

im_Y = double(zeros(fil, col));
im_Cb = double(zeros(fil, col));
im_Cr = double(zeros(fil, col));

Ysuma = 0.;
Cbsuma = 0;
Crsuma = 0;
MN = fil*col;

im_Y = double(im_YCbCr(:, :, 1));
im_Cb = double(im_YCbCr(:, :, 2));
im_Cr = double(im_YCbCr(:, :, 3));

% Promedios
for x = 1:fil
    for y = 1:col
        Ysuma  = im_Y(x, y)  + Ysuma;
        Cbsuma = im_Cb(x, y) + Cbsuma;
        Crsuma = im_Cr(x, y) + Crsuma;
    end
end


Yprom  = (Ysuma/MN);
Cbprom = (Cbsuma/MN);
Crprom = (Crsuma/MN);
 
Yprom = uint8(Yprom);
Cbprom = uint8(Cbprom);
Crprom = uint8(Crprom);

% Salida
for x = 1:fil
    for y = 1:col
        if im_Y(x, y) >= Yprom  &&  im_Cb(x, y) <= Cbprom  &&  im_Cr(x, y) >= Crprom
            im_filtro(x, y) = 1;
        else
            im_filtro(x, y) = 0;
        end
    end
end

imshow(im_filtro)
end