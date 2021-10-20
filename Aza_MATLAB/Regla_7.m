function output_image = Regla_7(input_image)

[fil, col, channel] = size(input_image);
output_image = double(zeros(fil, col));

imagen_Y = double(zeros(fil, col));
imagen_Cb = double(zeros(fil, col));
imagen_Cr = double(zeros(fil, col));

M = [0.2568, 0.5041, 0.0979; 
    -0.1482, -0.2910, 0.4392; 
    0.4392, -0.3678, -0.0714];

input_image = double(input_image);

Y  = 0.0;
Cb = 0.0;
Cr = 0.0;

for x = 1:fil
    for y = 1:col
        Y  = M(1,1)*input_image(x, y, 1) + M(1, 2)*input_image(x, y, 2) + M(1, 3)*input_image(x, y, 3) + 16;
        Cb = M(2,1)*input_image(x, y, 1) + M(2, 2)*input_image(x, y, 2) + M(2, 3)*input_image(x, y, 3) + 128;
        Cr = M(3,1)*input_image(x, y, 1) + M(3, 2)*input_image(x, y, 2) + M(3, 3)*input_image(x, y, 3) + 128;
        imagen_Y(x, y)  =  Y;
        imagen_Cb(x, y) =  Cb;
        imagen_Cr(x, y) =  Cr;
    end
end

for x = 1:fil
    for y = 1:col
        if imagen_Cb(x, y) <= 120  &&  imagen_Cr(x, y) >= 150
            output_image(x, y) = 1;
        else
            output_image(x, y) = 0;
        end
    end
end

% figure('Name','Imagen obtenida mediante regla 7','NumberTitle','off');
% imshow(output_image)
output_image = uint8(output_image);

end