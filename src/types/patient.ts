export type patientRow = [
  id: string,
  name: string,
  birthDate: string,
  gender: string,
  ...rest: string[],
]

export interface patientsResponse {
  patients: patientRow[]
}
