% Week 1 Exercise 1 for Phy 177
% Author: Francisco Gonzalez 
% SID: 861077407


% Inputting data given
Homework = [10, 10, 8, 9.5, 3, 9, 0, 6];
Midterm = [10, 10, 10, 10, 8, 5, 10, 7];
FinalProject = [9, 10, 10, 6, 10, 6, 8, 9];

% Set up matrix to put the results in
Grades = zeros(size(Homework));

% Fill up the Grades matrix using the formula G = 0.4*HW + 0.2*Midterm +
% 0.2*Project
for i = 1:length(Grades)
    Grades(i) = Homework(i)*0.4 + Midterm(i)*0.2 + FinalProject(i)*0.4;
end

% Open File called 'ex2.txt' and make it writable
fileID = fopen('ex2.txt','w');

% Print out the grades with two decimals
fprintf(fileID, '%6.2f \n',Grades);

fclose(fileID); % Close file

% Set up the variables for number of failed and outstanding students
nFailedStudents = 0;
nOutstandingStudents = 0;

% Count the number of failed and outstanding students
for i = 1:length(Grades)
    if Grades(i) < 6
        nFailedStudents = nFailedStudents + 1;
    end
    
    if Grades(i) > 9.5
        nOutstandingStudents = nOutstandingStudents + 1;
    end
end

% Print to screan the number of failed and outstanding students
fprintf('Fraction of outstanding students is: %d/%d\n',nOutstandingStudents,length(Grades));
fprintf('Number of failed students is: %d\n', nFailedStudents);

f = figure(1);
hist(Grades)
saveas(f,'HistogramEx2','jpg')
title 'Grades'
xlabel 'Score'
ylabel 'Number of students'






