% Week 1 Exercise 3a for Phy 177
% Author: Francisco Gonzalez 
% SID: 861077407

v = input('Enter initial velocity [m/s]: '); % request input
h = 800; % height of tower
g = 9.81; % m/s^2
syms t

time = solve(  h == 0.5*g*t^2 + v*t, t); % solve for t in d = 0.5gt^2 + vt
time = double(time);

for i = 1:length(time)
    if time(i) >= 0 && imag(time(i)) == 0
        fprintf('It will take%6.2f seconds to reach the ground\n',time(i)); %output the result
    end
end


% End Exercise 3a for Phy 177



