import subprocess
import time

# List of congestion control algorithms
congestion_algorithms = ["reno", "cubic", "highspeed", "bic", "scalable", "htcp", "vegas", "hybla", "lp", "illinois",   "veno",  "yeah", "westwood",    "bbr"]

# Output file to store results
output_file = "iperf_results.txt"

# Function to run iperf3 with a specified congestion control algorithm
def run_iperf_with_algorithm(algorithm):
    iperf_command = f"iperf3 -c <server_ip> -t 30 -C {algorithm}"
    result = subprocess.run(iperf_command, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout

# Run iperf3 with each congestion control algorithm
with open(output_file, "w") as file:
    for algorithm in congestion_algorithms:
        print(f"Running iperf3 with {algorithm}...")
        
        # Run iperf3 and get the result
        result = run_iperf_with_algorithm(algorithm)
        
        # Write the results to the output file with the algorithm name
        file.write(f"=== {algorithm} ===\n")
        file.write(result)
        file.write("\n\n")
        
        print(f"Finished running iperf3 with {algorithm}.\n")
        time.sleep(1)  # Add a short delay between tests to avoid interference

print(f"Results have been stored in {output_file}.")
