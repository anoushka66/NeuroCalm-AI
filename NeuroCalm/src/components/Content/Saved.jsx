import React, { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { useUser } from "@clerk/nextjs";
import Select from "react-select";

const SavedState = () => {
  const router = useRouter();
  const { isLoaded, isSignedIn } = useUser();

  const [stressLevel, setStressLevel] = useState("");
  const [age, setAge] = useState("");
  const [chronicDiseases, setChronicDiseases] = useState([]);
  const [recommendedTechniques, setRecommendedTechniques] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    if (isLoaded && !isSignedIn) {
      router.push("/sign-in");
    }
  }, [isLoaded, isSignedIn, router]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/management", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          stressLevel,
          age,
          chronicDiseases: chronicDiseases.map(disease => disease.value),
        }),
      });

      if (response.ok) {
        const result = await response.json();
        setRecommendedTechniques(result);
        setError("");
      } else {
        setError("Failed to fetch data");
      }
    } catch (error) {
      setError("An error occurred while fetching data");
    }
  };

  if (!isLoaded || !isSignedIn) {
    return <div>Loading...</div>;
  }

  const diseaseOptions = [
    { value: 'arthritis', label: 'Arthritis' },
    { value: 'diabetes', label: 'Diabetes' },
    { value: 'hypertension', label: 'Hypertension' },
    { value: 'asthma', label: 'Asthma' },
    { value: 'copd', label: 'Chronic Obstructive Pulmonary Disease (COPD)' },
    { value: 'fibromyalgia', label: 'Fibromyalgia' },
    { value: 'migraine', label: 'Migraine' },
    { value: 'osteoporosis', label: 'Osteoporosis' },
    { value: 'depression', label: 'Depression' },
    { value: 'ckd', label: 'Chronic Kidney Disease' },
    { value: 'ibs', label: 'Irritable Bowel Syndrome (IBS)' },
    { value: 'rheumatoid_arthritis', label: 'Rheumatoid Arthritis' },
    { value: 'multiple_sclerosis', label: 'Multiple Sclerosis' },
    { value: 'thyroid_disorders', label: 'Thyroid Disorders' },
    {value:'none',label:'None'}
  ];

  return (
    <div className="management-form mt-36 text-center mb-12 mx-auto max-w-4xl">
      <h1 className="text-7xl font-extrabold text-center text-white font-jost text-left">
        Neuro
        <span className="text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-violet-500">
          Calm
        </span>
      </h1>
      <h3 className="text-white text-lg text-center font-jost my-3 text-left">
        Management Recommendations
      </h3>
      <form onSubmit={handleSubmit} className="mt-6 mb-10 space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Enter Stress Level (0-4)
            </h4>
            <input
              className="bg-[rgba(255,255,255,0.2)] text-white outline-none p-3 rounded-full w-full"
              type="text"
              name="stressLevel"
              id="stressLevel"
              placeholder="Stress Level"
              value={stressLevel}
              onChange={(e) => setStressLevel(e.target.value)}
            />
          </div>
          <div>
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Enter Age
            </h4>
            <input
              className="bg-[rgba(255,255,255,0.2)] text-white outline-none p-3 rounded-full w-full"
              type="text"
              name="age"
              id="age"
              placeholder="Age"
              value={age}
              onChange={(e) => setAge(e.target.value)}
            />
          </div>
          <div className="col-span-2">
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Select Chronic Diseases
            </h4>
            <Select
              isMulti
              options={diseaseOptions}
              className="bg-[rgba(255,255,255,0.2)] text-black outline-none p-3 rounded-full w-full "

              onChange={(selectedOptions) => setChronicDiseases(selectedOptions)}
            />
          </div>
        </div>
        <button
          type="submit"
          className="bg-gradient-to-r from-pink-500 to-violet-500 text-white py-2 px-8 rounded-full"
        >
          Submit
        </button>
      </form>
      {error && <div className="text-red-500 mt-2">{error}</div>}
      {recommendedTechniques && (
        <div className="mt-10 text-white text-2xl">
          <h2>Recommended Management Techniques:</h2>
          {Object.entries(recommendedTechniques).map(([category, techniques]) => (
            <div key={category} className="mt-4">
              <h3 className="text-xl font-bold">{category}:</h3>
              <ul className="list-disc list-inside">
                {techniques.map((technique, index) => (
                  <li key={index}>{technique}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default SavedState;
