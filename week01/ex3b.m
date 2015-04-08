% Week 1 Exercise 3b for Phy 177
% Author: Francisco Gonzalez 
% SID: 861077407

height = 800; % meters
g = 9.81; % m/s^2
checkvalidity = 0;
% Take input from user
while checkvalidity == 0
    vmin = input('Enter minimum velocity: ');
    vmax = input('Enter maximum velocity: ');
    % Input sanitation
    if vmin < 0 
        errordlg('Vmin cannot be negative. Try again.')
    elseif vmax < 0
        errordlg('Vmax cannot be negative. Try again.')
    elseif vmin > vmax
        errordlg('Vmin cannot be larger than Vmax Try again.')
    else
        checkvalidity = 1;
    end
end

% make the bins and construct the time vector for later use
velocity = linspace(vmin,vmax,10);
time = zeros(size(velocity));

% uses solve element-wise to get the time vector filled that corresponds to
% the velocity vector
for i = 1:length(velocity)
    syms t
    temp = solve( height == 1/2*g*t^2 + velocity(i)*t,t);
    for j = 1:length(temp)
        if temp(j) >= 0 && imag(temp(j)) == 0
            time(i) = temp(j);
            break;
        end
    end
end

% Plot and make it pretty
f = figure(1);
plot(velocity, time)
title 'Initial Velocity vs Time it takes to hit Ground'
xlabel 'Velocity [m/s]'
ylabel 'Time [s]'

saveas(f,'PlotEx3b','jpg')

% Save the ASCII file
A = [ time; velocity ];
fileID = fopen('ex3b.txt','w');
fprintf(fileID,'%6s %9s \n','time','velocity');
fprintf(fileID,'%6.2f %6.2f \n',A);
fclose(fileID);












% End Week 1 Exercise 3b for Phy 177