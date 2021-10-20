function im_filtro = R4(im_rule_4)

[fil, col, ch] = size(im_rule_4);
im_YCbCr = rgb2ycbcr(im_rule_4);
im_filtro = double(zeros(fil, col));

for x = 1:fil
    for y = 1:col
        if im_YCbCr(x, y, 3) >= im_YCbCr(x, y, 2)
            im_filtro(x, y) = 1;
        else
            im_filtro(x, y) = 0;
        end
    end
end

imshow(im_filtro)
end