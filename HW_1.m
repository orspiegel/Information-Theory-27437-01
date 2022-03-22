%-----------------Details--------------------------%
% Name: Or Spiegel
% ID: 318720067
%----matrix of 10000 vectors from length of 50-----%
x = rand(50,10000);
y = prod(x);
%----SEMILOG represantation------------------------%
histogram(log(y));
xlabel('semilog y')
title('Random numbers')
%----mean calculation------------------------------%
mean_log_y = mean(log(y));
disp(['average of log(y) is: ' ,num2str(mean_log_y)]);
%----standard deviation calculation----------------%
disp(num2str(['standard deviation of log(y) is: ', ...
    num2str(std(log(y)))]));
