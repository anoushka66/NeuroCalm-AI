import React, { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { useUser } from "@clerk/nextjs";

const InputForm = () => {
  const router = useRouter();
  const { isLoaded, isSignedIn } = useUser();

  const [field1, setField1] = useState("");
  const [field2, setField2] = useState("");
  const [field3, setField3] = useState("");
  const [field4, setField4] = useState("");
  const [predictedStressLevel, setPredictedStressLevel] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    if (isLoaded && !isSignedIn) {
      router.push("/sign-in");
    }
  }, [isLoaded, isSignedIn, router]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          field1,
          field2,
          field3,
          field4,
        }),
      });

      if (response.ok) {
        const result = await response.json();
        setPredictedStressLevel(result.predictedStressLevel);
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

  return (
    <div className="input-form mt-36 text-center mb-12 mx-auto max-w-4xl">
      <h1 className="text-7xl font-extrabold text-center text-white font-jost text-left">
        Neuro
        <span className="text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-violet-500">
          Calm
        </span>
      </h1>
      <h3 className="text-white text-lg text-center font-jost my-3 text-left">
        Detect using ML Models
      </h3>
      <form onSubmit={handleSubmit} className="mt-6 mb-10 space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Enter Snoring Rate
            </h4>
            <input
              className="bg-[rgba(255,255,255,0.2)] text-white outline-none p-3 rounded-full w-full"
              type="text"
              name="field1"
              id="field1"
              placeholder="Field 1"
              value={field1}
              onChange={(e) => setField1(e.target.value)}
            />
          </div>
          <div>
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Enter Respiration Rate
            </h4>
            <input
              className="bg-[rgba(255,255,255,0.2)] text-white outline-none p-3 rounded-full w-full"
              type="text"
              name="field2"
              id="field2"
              placeholder="Field 2"
              value={field2}
              onChange={(e) => setField2(e.target.value)}
            />
          </div>
          <div>
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Enter Blood Oxygen Level
            </h4>
            <input
              className="bg-[rgba(255,255,255,0.2)] text-white outline-none p-3 rounded-full w-full"
              type="text"
              name="field3"
              id="field3"
              placeholder="Field 3"
              value={field3}
              onChange={(e) => setField3(e.target.value)}
            />
          </div>
          <div>
            <h4 className="text-white text-md font-medium mb-2 text-left">
              Enter Heart Rate
            </h4>
            <input
              className="bg-[rgba(255,255,255,0.2)] text-white outline-none p-3 rounded-full w-full"
              type="text"
              name="field4"
              id="field4"
              placeholder="Field 4"
              value={field4}
              onChange={(e) => setField4(e.target.value)}
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
      {predictedStressLevel !== null && (
        <div className="mt-10 text-white text-2xl">
          Predicted Stress Level: {predictedStressLevel}
          <meter
            min="0"
            max="4"
            value={predictedStressLevel}
            className="w-full h-8 bg-[rgba(255,255,255,0.2)] bg-gradient-to-r from-pink-500 to-violet-500  rounded-full overflow-hidden mt-4"
          ></meter>
        </div>
      )}
    </div>
  );
};

export default InputForm;