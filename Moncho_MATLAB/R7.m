function im_filtro = R7(im_rule_7)

[fil, col, ch] = size(im_rule_7);
im_YCbCr = rgb2ycbcr(im_rule_7);
im_filtro = double(zeros(fil, col));

for x = 1:fil
    for y = 1:col
        if im_YCbCr(x, y, 2) <= 120  &&  im_YCbCr(x, y, 3) >= 150
            im_filtro(x, y) = 1;
        else
            im_filtro(x, y) = 0;
        end
    end
end

imshow(im_filtro)
end