% LinearSystemSolve.m %MATLAB M-file
n = 3; % n interior points
N = n+2; % includes the two ends points
H = 1; % Radius of the channel
L = 5; % Length of the channel
DeltaP = 8.0; % Pressure drop
nu = 0.42;% Viscosity
Vmax =(DeltaP*H^2)/(2*nu*L); % Maximum value of V(y)
A = [2, -1, 0; -1, 2, -1; 0, -1, 2];
dy=(2*H)/(n+1);
f(1:n)=(dy^2)*(2*Vmax)/(H^2); % In terms of Vmax
% Or,
f(1:n)=(dy^2)*DeltaP/(nu*L); % In terms of pressure
for i = 1:n
yj(i) =-H+i*dy;
V_exact(i)=Vmax*(1-(yj(i)/H)^2); % Exact solution
end
sol= A\f; %MATLAB backslash ’\’ command
finalsol= [yj sol V_exact];
disp(finalsol) % Solution for only interior points
