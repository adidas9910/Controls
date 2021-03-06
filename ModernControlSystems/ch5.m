% Modern Control System 13th Edition
% Page 342

Ka = [10:10:60]';
for ii = 1:length(Ka)
    t = [0:0.01:1];
    nc = [Ka(ii)*5];
    dc = [1];
    sysc = tf(nc, dc);
    ng = [1];
    dg = [1, 20, 0];
    sysg = tf(ng, dg);
%     % For tracking set-point 
%     sys1 = series(sysc, sysg);
%     sys = feedback(sys1, [1]);
    % For rejecting disturbance 
    sys1 = feedback(sysg, sysc);
    sys = -sys1;
    
    y = step(sys, t);
    plot(t, y); grid on;
    xlabel('Time(s)');
    ylabel('y(t)');
    hold on;
end
legend([repmat('Ka = ',size(Ka)),num2str(Ka)])


