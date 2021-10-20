function im_filtro = R1(im_rule_1)

[fil, col, ch] = size(im_rule_1);

im_filtro = double(zeros(fil, col));

for x = 1:fil
    for y = 1:col
        if (im_rule_1(x, y, 2) > im_rule_1(x, y, 3))
            if (im_rule_1(x, y, 1) > im_rule_1(x, y, 2))
                im_filtro(x, y) = 1;
            end
        else
            im_filtro(x, y) = 0;
        end
    end
end

 imshow(im_filtro) 
end 

