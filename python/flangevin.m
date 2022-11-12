function [dx,vi] = flangevin(T, a, m, dt, N, D, vi)
%function x = Langevin(T,a, m, dt, N, D, vi)
%Modelling Langevin Motion, returns trajectories of x(t) for single
%realization of white noise u(t).
%%
%T: Temperature in Kelvins 
%a: Particle Radius in um
%m: mass of particle
%N: timesteps
%dt: interval between timesteps
%D: diffusion 
%vi: initial velocity of particle
%%
a = a*1e-6;
h=6.6262e-34;            %Plancks Constant (Js)
kb=1.3806503e-23;        %Boltzmann Constant (J/K)
n=fviscosity(T)*1e-6;    %return the viscosity for pure water (uPa.s)
%t=dt:dt:(dt*(N));        %[h, 2h, 3h, 4h] timesteps
%%
v=zeros(1,N); %container of velocities
v(1)=vi; %initial velocity.
alpha = 6*pi()*n*a;
qconst = -alpha/m;   %coefficient of drift term
gconst = 1.0/m;             %coefficient of diffusion term
sigma = sqrt(2*kb*T*alpha);       %noise strength
k = gconst*sqrt(dt)*sigma;
k2 = dt*qconst;
%%
for i=1:length(v)-1
    v(i+1) = v(i) + k2*v(i)+ k*randn;   
end
%%obtaining the x trajectories from v datapoints
dx = v.*dt;
vi = v(length(v));
end