import numpy as np

def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    
    values, counts = np.unique(data, return_counts=True)
    if np.max(counts) > 1:
        mode = values[np.argmax(counts)]
    else:
        mode = 'No hay moda'
    
    range_ = np.ptp(data)
    variance = np.var(data)
    std_deviation = np.std(data)
    coefficient_variation = (std_deviation / mean) * 100 if mean != 0 else float('nan')

    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': range_,
        'variance': variance,
        'std_deviation': std_deviation,
        'coefficient_variation': coefficient_variation
    }
