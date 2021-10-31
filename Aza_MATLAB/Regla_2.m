function output_image = Regla_2(input_image)

[fil, col, channel] = size(input_image);
output_image = double(zeros(fil, col));

for x = 1:fil
    for y = 1:col
        if input_image(x, y, 1) > 190  &&  input_image(x, y, 2) > 100  &&  input_image(x, y, 3) < 140
            output_image(x, y) = 1;
        else
            output_image(x, y) = 0;
        end
    end
end

figure('Name','Imagen obtenida mediante regla 2','NumberTitle','off');
imshow(output_image)
output_image = uint8(output_image);

end