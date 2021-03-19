%% Example on page 21-22
A = [4/3, -2/3; 1, 0];
B = [1; 0];
C = [-2/3, 1];

sys_ss = ss(A, B, C, 0);
sys_zpk = zpk(sys);
sys_zpk.z

Q = C'*C + 0.001*eye(2);
R = 0.001;

N = 70;
PAI = cell(N,1); % from N to 1
K = cell(N,1); % from N-1 to 0

PAI{end} = Q;
for k = N-1:-1:1
    PAI{k} = Q + A'*PAI{k+1}*A - A'*PAI{k+1}*B*inv(B'*PAI{k+1}*B+R)*B'*PAI{k+1}*A; % Equation 1.10 
end

for k = N:-1:1
    K{k} = -inv(B'*PAI{k}*B+R)*B'*PAI{k}*A;
end

eig(A+B*K{1})
