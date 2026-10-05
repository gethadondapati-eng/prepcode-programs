students = int(input("enter the students: "))
each_bench_students = 3
total_bench_student = students // each_bench_students
remaining_students = students % each_bench_students
print(f"total_bench_student:{total_bench_student},remaining_students:{remaining_students}")