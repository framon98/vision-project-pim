function im_filtro = R2(im_rule_2)

[fil, col, ch] = size(im_rule_2);

im_filtro = double(zeros(fil, col));

for x = 1:fil
    for y = 1:col
        if im_rule_2(x, y, 1) > 190 && im_rule_2(x, y, 2) > 100 && im_rule_2(x, y, 3) < 140
            im_filtro(x, y) = 1;
        else
            im_filtro(x, y) = 0;
        end
    end
end

imshow(im_filtro)
end 