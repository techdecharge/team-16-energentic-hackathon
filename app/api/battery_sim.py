from fastapi import APIRouter

router = APIRouter()

import json
battery_data ={
  "battery_specifications": {
    "battery_type": "Lithium-ion (LiFePO4)",
    "total_capacity_kWh": 10,
    "usable_capacity_kWh": 9.5,
    "nominal_voltage_V": 48,
    "max_charging_power_kW": 5,
    "max_discharging_power_kW": 5,
    "round_trip_efficiency_percent": 92,
    "soc_range_percent": {
      "min": 5,
      "max": 100
    },
    "installation": "Single household rooftop solar system",
    "coupling": "AC-coupled"
  },
  "simulation_data": [
    { "time": "00:00", "solar_input_kW": 0.0, "load_kW": 0.6, "battery_soc_percent": 85, "charge_discharge_kW": -0.6, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "01:00", "solar_input_kW": 0.0, "load_kW": 0.4, "battery_soc_percent": 82, "charge_discharge_kW": -0.4, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "02:00", "solar_input_kW": 0.0, "load_kW": 0.3, "battery_soc_percent": 80, "charge_discharge_kW": -0.3, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "03:00", "solar_input_kW": 0.0, "load_kW": 0.3, "battery_soc_percent": 78, "charge_discharge_kW": -0.3, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "04:00", "solar_input_kW": 0.0, "load_kW": 0.5, "battery_soc_percent": 75, "charge_discharge_kW": -0.5, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "05:00", "solar_input_kW": 0.0, "load_kW": 0.7, "battery_soc_percent": 71, "charge_discharge_kW": -0.7, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "06:00", "solar_input_kW": 0.2, "load_kW": 0.9, "battery_soc_percent": 66, "charge_discharge_kW": -0.7, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "07:00", "solar_input_kW": 0.8, "load_kW": 1.1, "battery_soc_percent": 60, "charge_discharge_kW": -0.3, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "08:00", "solar_input_kW": 1.5, "load_kW": 1.0, "battery_soc_percent": 61, "charge_discharge_kW": 0.5, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "09:00", "solar_input_kW": 2.5, "load_kW": 0.9, "battery_soc_percent": 65, "charge_discharge_kW": 1.6, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "10:00", "solar_input_kW": 3.2, "load_kW": 0.8, "battery_soc_percent": 72, "charge_discharge_kW": 2.4, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "11:00", "solar_input_kW": 4.0, "load_kW": 1.0, "battery_soc_percent": 80, "charge_discharge_kW": 2.8, "grid_import_kW": 0.0, "grid_export_kW": 0.2 },
    { "time": "12:00", "solar_input_kW": 4.2, "load_kW": 0.9, "battery_soc_percent": 88, "charge_discharge_kW": 2.3, "grid_import_kW": 0.0, "grid_export_kW": 1.0 },
    { "time": "13:00", "solar_input_kW": 3.8, "load_kW": 0.8, "battery_soc_percent": 95, "charge_discharge_kW": 1.2, "grid_import_kW": 0.0, "grid_export_kW": 1.8 },
    { "time": "14:00", "solar_input_kW": 3.5, "load_kW": 1.1, "battery_soc_percent": 100, "charge_discharge_kW": 0.0, "grid_import_kW": 0.0, "grid_export_kW": 2.4 },
    { "time": "15:00", "solar_input_kW": 2.5, "load_kW": 1.0, "battery_soc_percent": 100, "charge_discharge_kW": 0.0, "grid_import_kW": 0.0, "grid_export_kW": 1.5 },
    { "time": "16:00", "solar_input_kW": 1.5, "load_kW": 1.2, "battery_soc_percent": 98, "charge_discharge_kW": -0.3, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "17:00", "solar_input_kW": 0.8, "load_kW": 1.5, "battery_soc_percent": 95, "charge_discharge_kW": -0.7, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "18:00", "solar_input_kW": 0.2, "load_kW": 1.8, "battery_soc_percent": 90, "charge_discharge_kW": -1.6, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "19:00", "solar_input_kW": 0.0, "load_kW": 2.0, "battery_soc_percent": 82, "charge_discharge_kW": -2.0, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "20:00", "solar_input_kW": 0.0, "load_kW": 1.5, "battery_soc_percent": 76, "charge_discharge_kW": -1.5, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "21:00", "solar_input_kW": 0.0, "load_kW": 1.0, "battery_soc_percent": 73, "charge_discharge_kW": -1.0, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "22:00", "solar_input_kW": 0.0, "load_kW": 0.7, "battery_soc_percent": 71, "charge_discharge_kW": -0.7, "grid_import_kW": 0.0, "grid_export_kW": 0.0 },
    { "time": "23:00", "solar_input_kW": 0.0, "load_kW": 0.6, "battery_soc_percent": 69, "charge_discharge_kW": -0.6, "grid_import_kW": 0.0, "grid_export_kW": 0.0 }
  ]
}


@router.get("/battery/details")
def fetch_battery_details():
    return battery_data


@router.get("/battery/command/start_discharge")
def battery_discharge_command():
    return "Discharge from the battery to grid is initiated."
